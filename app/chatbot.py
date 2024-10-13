from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the smaller pre-trained model and tokenizer from Hugging Face
model_name = "EleutherAI/gpt-neo-125M"  # Using the smallest GPT-Neo model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Set device to GPU if available, else use CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Function to generate a chatbot response using the LLM
def generate_response(input_text):
    try:
        # Encode input text
        inputs = tokenizer(input_text, return_tensors="pt").to(device)

        # Generate response (you can set max length and temperature for control)
        outputs = model.generate(inputs.input_ids, max_length=50)

        # Decode the generated response back to text
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)

        return response
    except Exception as e:
        return f"Error: {str(e)}"
