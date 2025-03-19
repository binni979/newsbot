from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from app.scraper import scrape_latest_news

# Load the smaller pre-trained model and tokenizer from Hugging Face
model_name = 'distilgpt2'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Set device to GPU if available, else use CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

def truncate_incomplete_articles(text):
    """Ensure the last displayed article is fully complete."""
    delimiter = "=" * 40  # Used to separate articles
    articles = text.split(delimiter)

    # Check if the last article is incomplete
    last_article = articles[-1].strip()
    if not last_article.endswith("Z"):  # Published date usually ends with 'Z'
        articles.pop()  # Remove the incomplete article

    return delimiter.join(articles).strip()

def generate_response(input_text):
    try:
        news_articles = scrape_latest_news(input_text)

        if not news_articles:
            return "Sorry, I couldn't find any recent news on this topic."

        news_context = "\n".join(
            f"Title: {article['title']}\nDescription: {article['description']}\nURL: {article['url']}\nSource: {article['source']}\nPublished At: {article['publishedAt']}\n{'=' * 40}"
            for article in news_articles
        )

        combined_input = f"{news_context}\n\nChatbot:"

        inputs = tokenizer(combined_input, return_tensors="pt", padding=True, truncation=True, max_length=512).to(device)

        outputs = model.generate(
            inputs.input_ids,
            attention_mask=inputs.attention_mask,
            max_new_tokens=150,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            top_k=40,
            pad_token_id=tokenizer.eos_token_id,
        )

        response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
        return truncate_incomplete_articles(response)

    except Exception as e:
        return f"Error: {str(e)}"
