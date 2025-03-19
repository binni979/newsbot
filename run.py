import gradio as gr
from threading import Thread
from app.chatbot import generate_response
from app.routes import app

# Gradio interface for the chatbot
def gradio_chatbot(input_text):
    response = generate_response(input_text)
    return response

# Initialize Gradio interface with updated settings
gradio_interface = gr.Interface(
    fn=gradio_chatbot,
    inputs=gr.Textbox(
        label="Enter your query here",
        placeholder="Type something here...",
        lines=3,
        max_length=500
    ),
    outputs=[gr.Textbox(
        label="Chatbot Response",
        placeholder="The chatbot's response will appear here...",
        lines=5,
        interactive=False
    )],
    title="NewsBot Chatbot",
    description="A chatbot that provides recent news articles based on your queries. Just type your topic and get the latest updates!",
    allow_flagging="never",
    live=False,
)

def run_gradio():
    # Set share=False to keep the interface private
    gradio_interface.launch(share=False)

if __name__ == "__main__":
    # Start Flask and Gradio in separate threads
    flask_thread = Thread(target=run_gradio)
    flask_thread.start()
    app.run(port=5000, debug=False, threaded=False)
