import streamlit as st
import joblib
st.title("Review Detector")
reload_model = joblib.load("Review_Classifier")

ip = st.text_input("Enter your Review : ")
op = reload_model.predict([ip])

if st.button("Detect"):
  st.title(op[0])
