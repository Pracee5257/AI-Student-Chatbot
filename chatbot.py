import gradio as gr
from groq import Groq

client = Groq(api_key="PASTE_YOUR_GROQ_KEY")

def chatbot(You):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a helpful student assistant."},
            {"role": "user", "content": You}
        ]
    )

    return response.choices[0].message.content


interface = gr.Interface(
    fn=chatbot,
    inputs="text",
    outputs="text",
    title="AI Student Chatbot"
)

interface.launch(share=True)
