import streamlit as st
import pickle
import numpy as np

# Load all models from the pickle file
@st.cache_resource
def load_models():
    try:
        with open("models.pkl", "rb") as file:
            models = pickle.load(file)
            return models
    except Exception as e:
        st.error(f"Error loading models: {e}")
        st.stop()

# Load the models
models = load_models()

# Streamlit form for user input
st.title("Customer Churn Prediction")
st.subheader("Enter customer details to predict churn:")

# Collect user input
international_plan = st.selectbox("International Plan", ("Yes", "No"))
voice_mail_plan = st.selectbox("Voice Mail Plan", ("Yes", "No"))
total_day_minutes = st.number_input("Total Day Minutes", min_value=0.0, step=0.1)  # Accepts decimal values
total_day_calls = st.number_input("Total Day Calls", min_value=0.0, step=0.1)      # Accepts decimal values
total_eve_minutes = st.number_input("Total Evening Minutes", min_value=0.0, step=0.1)  # Accepts decimal values
total_eve_calls = st.number_input("Total Evening Calls", min_value=0.0, step=0.1)      # Accepts decimal values
total_night_minutes = st.number_input("Total Night Minutes", min_value=0.0, step=0.1)  # Accepts decimal values
total_night_calls = st.number_input("Total Night Calls", min_value=0.0, step=0.1)      # Accepts decimal values
total_intl_minutes = st.number_input("Total International Minutes", min_value=0.0, step=0.1)  # Accepts decimal values
total_intl_calls = st.number_input("Total International Calls", min_value=0.0, step=0.1)      # Accepts decimal values
number_customer_service_calls = st.number_input("Number of Customer Service Calls", min_value=0.0, step=0.1)  # Accepts decimal values

# Map categorical inputs to numerical values
international_plan = 1 if international_plan == "Yes" else 0
voice_mail_plan = 1 if voice_mail_plan == "Yes" else 0

# Create the input data array
input_data = np.array([[international_plan, voice_mail_plan, total_day_minutes, total_day_calls,
                        total_eve_minutes, total_eve_calls, total_night_minutes, total_night_calls,
                        total_intl_minutes, total_intl_calls, number_customer_service_calls]])

# Let the user select a model
model_choice = st.selectbox("Select a model for prediction:", list(models.keys()))

# Predict and display the result using the selected model
if st.button("Predict Churn"):
    model = models[model_choice]  # Select the model based on user input
    prediction = model.predict(input_data)
    
    if prediction == 1:
        st.write(f"The customer is likely to churn (Predicted using {model_choice}).")
    else:
        st.write(f"The customer is unlikely to churn (Predicted using {model_choice}).")