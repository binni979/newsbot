from flask import Flask, jsonify, request
from app.chatbot import generate_response
from app.scraper import scrape_latest_news


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify({"status": "OK"}), 200

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