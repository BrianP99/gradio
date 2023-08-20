import gradio as gr

def greet(name):
    return 'Hi, ' +name
app = gr.Interface(
    inputs="text",
    fn=greet,
    outputs="text"
)

app.launch(share=True)