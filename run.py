import gradio as gr
from threading import Thread
from app.chatbot import generate_response
from app.routes import app

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
    app.run(port=5000, debug=True, threaded=False)

def run_gradio():
    # Set share=True for public access
    gradio_interface.launch(share=False)

if __name__ == "__main__":
    # Start Flask and Gradio in separate threads
    flask_thread = Thread(target=run_flask)
    flask_thread.start()
    run_gradio()

