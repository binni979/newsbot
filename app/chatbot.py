from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from app.scraper import scrape_latest_news

# Load the GPT-J model and tokenizer from Hugging Face
model_name = "EleutherAI/gpt-j-6B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Set a pad token as EOS token
tokenizer.pad_token = tokenizer.eos_token

# If you want to add a custom padding token:
# tokenizer.add_special_tokens({'pad_token': '[PAD]'})
# model.resize_token_embeddings(len(tokenizer))  # This is necessary if you add new tokens

# Set device to GPU if available, else use CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Function to generate a chatbot response using the GPT-J model with news context
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

        # Encode input text with attention mask
        inputs = tokenizer(combined_input, return_tensors="pt", padding=True).to(device)
        print ('yo')
        # Generate response
        outputs = model.generate(
            input_ids=inputs.input_ids,
            attention_mask=inputs.attention_mask,  # Ensure attention mask is set
            max_new_tokens=50,  # Adjust this value for response length
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
