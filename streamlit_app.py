import streamlit as st
import openai
from huggingface_hub.inference_api import InferenceApi

inference = InferenceApi(repo_id="microsoft/BioGPT-Large", token="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")
inference = InferenceApi(repo_id="microsoft/BioGPT-Large-PubMedQA", token="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")
result = inference(inputs="COVID-19 is ")
print(result[0]['generated_text'])


result = inference(inputs="What are the top 3 takeaways about COVID-19?")
print(result[0]['generated_text'])


# Set up the page layout
st.title("Text Input Demo")
st.write("Enter some text and click the button to see the output.")

# Create a text box for input
input_text = st.text_input("Enter your text here:")

# Create a submit button and a reset button
col1, col2 = st.beta_columns(2)
if col1.button("Submit"):
    # Process the input text
    output_text = input_text.upper()

    # Display the output text
    st.write("Output text:")
    st.write(output_text)

if col2.button("Reset"):
    # Clear the input and output
    input_text = ""
    output_text = ""
    st.write("Input and output cleared.")

'''
# Show the output text
if output_text:
    st.write("Output text:")
    st.write(output_text)
'''
