from flask import Flask, jsonify, request
import gradio as gr
from threading import Thread
from app.chatbot import generate_response
from app.scraper import scrape_latest_news

# Initialize Flask app
app = Flask(__name__)

# Flask route for health check
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "OK"}), 200

# Flask route to scrape news
@app.route('/scrape_news', methods=['POST'])
def scrape_news():
    try:
        scraped_data = scrape_latest_news()
        return jsonify({"message": "News scraped successfully!", "data": scraped_data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Flask route for chatbot response
@app.route('/chatbot', methods=['POST'])
def chatbot_response():
    try:
        user_input = request.json.get('text', '')
        if not user_input:
            return jsonify({"error": "No input text provided"}), 400
        
        response = generate_response(user_input)
        return jsonify({"response": response}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Gradio interface for the chatbot
def gradio_chatbot(input_text):
    response = generate_response(input_text)
    return response

# Initialize Gradio interface
gradio_interface = gr.Interface(
    fn=gradio_chatbot,
    inputs="text",
    outputs="text"
)

# Function to run Flask app
def run_flask():
    app.run(port=5000)

# Function to run Gradio interface
def run_gradio():
    gradio_interface.launch(share=True)  # Set share=True if you want public access

if __name__ == "__main__":
    # Start Flask and Gradio in separate threads
    flask_thread = Thread(target=run_flask)
    flask_thread.start()
    
    run_gradio()  # This will block the main thread
