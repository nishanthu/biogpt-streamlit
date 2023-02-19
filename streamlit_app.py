import streamlit as st
import openai
from huggingface_hub.inference_api import InferenceApi

def main():
    inference = InferenceApi(repo_id="microsoft/BioGPT-Large-PubMedQA", token="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")
    st.title("BioGPT App")

    with st.form(key="qa_input_form", clear_on_submit=True):
        input_text = st.text_input("Enter your question here:")
        submit_button = st.form_submit_button("Submit")

    if submit_button:
        st.write("Question: " + input_text)
        result = inference(inputs=input_text)
        st.write("Answer: " + result[0]['generated_text'])

if __name__ == "__main__":
    main()
