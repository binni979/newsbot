from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from app.scraper import scrape_latest_news

# Load the smaller pre-trained model and tokenizer from Hugging Face
model_name = "EleutherAI/gpt-j-6B" 
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Set device to GPU if available, else use CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Function to generate a chatbot response using the LLM with news context
def generate_response(input_text):
    try:
        # Get the latest news articles
        news_articles = scrape_latest_news()
        
        # Create a context string from the latest news
        news_context = "\n".join(
            f"Title: {article['title']}\nDescription: {article['description']}\nURL: {article['url']}" 
            for article in news_articles
        )
        
        # Combine the user's input with the news context
        combined_input = f"User: {input_text}\n\nLatest News:\n{news_context}\n\nChatbot:"

        # Encode input text
        inputs = tokenizer(combined_input, return_tensors="pt").to(device)

        # Generate response
        outputs = model.generate(
            inputs.input_ids,
            attention_mask=inputs.attention_mask,
            max_new_tokens=100,
            temperature=0.9,  # Adjust temperature for diversity
            top_p=0.95,       # Increase top-p for nucleus sampling
            top_k=50,         # Increase top-k for more diverse outputs
            pad_token_id=tokenizer.eos_token_id,
        )
        response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

        # Check if "Chatbot:" exists before splitting
        if "Chatbot:" in response:
            response_text = response.split("Chatbot:")[-1].strip()
        else:
            response_text = response.strip()  # Use the full response if "Chatbot:" is missing
        
        return response_text
    except Exception as e:
        return f"Error: {str(e)}"
