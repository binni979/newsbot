from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from app.scraper import scrape_latest_news

# Load the smaller pre-trained model and tokenizer from Hugging Face
model_name = "EleutherAI/gpt-neo-125M"  # Using the smallest GPT-Neo model
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
            max_new_tokens=50,  # Adjust this value as needed for response length
            num_return_sequences=1,
            pad_token_id=tokenizer.eos_token_id,  # Set pad_token_id to eos_token_id
        )

        # Decode the generated response back to text
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Extract the response from the chatbot
        response_text = response.split("Chatbot:")[-1].strip()  # Get only the chatbot's response
        
        return response_text
    except Exception as e:
        return f"Error: {str(e)}"
