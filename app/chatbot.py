import logging
import re
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from app.scraper import scrape_latest_news

# Configure logging
logging.basicConfig(level=logging.ERROR)

# Load model and tokenizer
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model_name = "distilgpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name).to(device)

# Set pad token if missing
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token


def truncate_incomplete_articles(text):
    """Ensure the last displayed article is fully complete."""
    delimiter = "=" * 40
    articles = text.split(delimiter)

    valid_timestamp_regex = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
    if not valid_timestamp_regex.search(articles[-1]):
        articles.pop()

    return delimiter.join(articles).strip()


def generate_response(input_text):
    try:
        news_articles = scrape_latest_news(input_text)

        if not isinstance(news_articles, list) or not all(isinstance(a, dict) for a in news_articles):
            return "Received an unexpected response while fetching news."

        if not news_articles:
            return "Sorry, I couldn't find any recent news on this topic."

        news_context = "\n".join(
            f"Title: {article.get('title', 'N/A')}\nDescription: {article.get('description', 'N/A')}\nURL: {article.get('url', 'N/A')}\nSource: {article.get('source', 'N/A')}\nPublished At: {article.get('publishedAt', 'N/A')}\n{'=' * 40}"
            for article in news_articles
        )

        combined_input = f"{news_context}\n\nChatbot:"
        max_input_length = tokenizer.model_max_length  # Dynamically fetch model's limit

        inputs = tokenizer(
            combined_input,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=min(len(combined_input.split()), max_input_length)
        ).to(device)

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
        logging.error(f"Error generating response: {str(e)}", exc_info=True)
        return "Oops! Something went wrong while processing your request."


# Example usage
if __name__ == "__main__":
    user_input = "latest technology news"
    print(generate_response(user_input))
