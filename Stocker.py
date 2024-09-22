import os
import streamlit as st
from ibm_watsonx_ai.foundation_models import Model
import getpass

# Function to get credentials
def get_credentials():
    return {
        "url": "https://us-south.ml.cloud.ibm.com",
        "apikey": getpass.getpass("Please enter your API key: ")
    }

# Initialize Streamlit app
st.title("Sentiment Analysis with Watsonx.ai")

# Input fields for API Key and Project ID
api_key = st.text_input("API Key", type="password")
project_id = st.text_input("Project ID")

# Space ID preset to None
space_id = None

# Input text for the prompt
prompt_input = st.text_area("Enter your news headline:")

# Button to submit the request
if st.button("Analyze Sentiment"):
    if api_key and project_id:
        # Set parameters
        model_id = "google/flan-t5-xxl"
        parameters = {
            "decoding_method": "greedy",
            "max_new_tokens": 100,
            "repetition_penalty": 2
        }

        # Create the model object
        model = Model(
            model_id=model_id,
            params=parameters,
            credentials={"url": "https://us-south.ml.cloud.ibm.com", "apikey": api_key},
            project_id=project_id,
            space_id=space_id  # Space ID is preset to None
        )

        # Submit the prompt for generation
        st.write("Submitting generation request...")
        generated_response = model.generate_text(prompt=prompt_input+". Give a Sentiment Analysis of this statement (is it good for the company or the country).", guardrails=True)
        generated_response1 = model.generate_text(prompt=prompt_input+". Give a summary of this statement.", guardrails=True)


        # Display the response
        st.write("Response:")
        st.write(generated_response)
        st.write(generated_response1)
    else:
        st.error("Please enter both API Key and Project ID.")

        