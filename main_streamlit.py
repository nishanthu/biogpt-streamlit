import streamlit as st
import openai
from huggingface_hub.inference_api import InferenceApi

inference = InferenceApi(repo_id="microsoft/BioGPT-Large", token="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")
inference(inputs="COVID-19 is ")

