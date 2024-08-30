import pickle
import asyncio
import gradio as gr
from model import chain
from vectorstore import vector_store
from preprocessing import clean_text

# importing the retriever
retriever = vector_store()


async def healthcare(text):
    if not text.strip():
        return None, gr.Warning("Please enter a text to convert.")
    



    docs = retriever.get_relevant_documents(text)

    # Assuming `chain.invoke` is a synchronous function. If it's asynchronous, use `await chain.invoke(...)`
    ans = chain.invoke({"context": docs, "question": text})
    
    # Apply the cleaning function
    cleaned_text = clean_text(ans)

    # Join the cleaned lines into a single string for output
    final_output = "\n".join(cleaned_text)
    return final_output

# Gradio interface
def gradio_interface(text):
    # Running the async healthcare function in the event loop
    output = asyncio.run(healthcare(text))
    return output

# Gradio application
def gradio_app():
    app = gr.Interface(
        fn=gradio_interface,
        inputs="textbox",
        outputs="textbox",
        title="Health Care Assistant Using RAG",
        description="AI Healthcare Assistant offering instant, accurate insights on diseases, symptoms, and treatments for personalized care.",
        analytics_enabled=False,
        allow_flagging=False
    )
    return app

if __name__ == "__main__":
    demo = gradio_app()
    demo.launch()