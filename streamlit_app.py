import streamlit as st
import openai
from huggingface_hub.inference_api import InferenceApi

inference = InferenceApi(repo_id="microsoft/BioGPT-Large", token="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")
inference = InferenceApi(repo_id="microsoft/BioGPT-Large-PubMedQA", token="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")
result = inference(inputs="COVID-19 is ")
print(result[0]['generated_text'])


result = inference(inputs="What are the top 3 takeaways about COVID-19?")
print(result[0]['generated_text'])



def main():
    st.title("BioGPT App")

    with st.form(key="qa_input_form", clear_on_submit=True):
        input_text = st.text_input("Enter your question here:")
        submit_button = st.form_submit_button("Submit")

    if submit_button:
        output_text = input_text.upper()
        st.write(output_text)

if __name__ == "__main__":
    main()
