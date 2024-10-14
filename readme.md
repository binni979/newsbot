# News Chatbot with GPT-J and Flask

This project integrates a chatbot powered by the GPT-J-6B language model with a Flask API. The chatbot provides responses using both user inputs and the latest news context from web scraping. Gradio is used for the user interface, and the project includes a simple news scraper for retrieving dummy news data.

## Features

- **News Scraping**: Scrapes the latest news articles (currently uses static dummy data).
- **GPT-J-6B Model**: Utilizes the GPT-J-6B model for chatbot responses with news context.
- **Flask API**: Provides REST API endpoints for chatbot responses and scraping.
- **Gradio Interface**: Interactive interface for chatting with the bot.

## Requirements

- Python 3.8+
- Pip dependencies listed in the `requirements.txt` file.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/news-chatbot.git
    cd news-chatbot
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Download the GPT-J model and tokenizer:
    ```python
    from transformers import AutoModelForCausalLM, AutoTokenizer

    model_name = "EleutherAI/gpt-j-6B"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    ```

## Running the Application

### Start the Flask API

1. Run the Flask server:
    ```bash
    python run.py
    ```

2. The Flask server will start on `http://localhost:5000`.

### Start the Chatbot UI (Gradio)

1. The Gradio interface will launch automatically when Flask starts. You can access the chatbot UI at `http://localhost:7860`.

## API Endpoints

- **Health Check**: `/health`
  - **Method**: GET
  - **Response**: `{ "status": "OK" }`

- **Scrape News**: `/scrape_news`
  - **Method**: POST
  - **Response**: Scrapes the latest news articles (dummy data).

- **Chatbot**: `/chatbot`
  - **Method**: POST
  - **Body**: `{ "text": "<User Input>" }`
  - **Response**: The chatbot's generated response using the GPT-J model.

## Example Usage

### Interacting with the Chatbot

To interact with the chatbot, either use the Gradio interface or send a POST request to the `/chatbot` endpoint:

```bash
curl -X POST http://localhost:5000/chatbot -H "Content-Type: application/json" -d '{"text": "What is the latest news?"}'


├── app
│   ├── __init__.py
│   ├── chatbot.py         # Chatbot model and response generation
│   ├── scraper.py         # News scraping logic (dummy data)
├── run.py                 # Main entry point to run Flask and Gradio
├── requirements.txt       # List of dependencies
├── README.md              # Project documentation
