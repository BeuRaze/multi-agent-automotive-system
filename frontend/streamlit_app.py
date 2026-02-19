import streamlit as st
import requests

st.set_page_config(page_title="Automotive AI", layout="centered")

st.title("🚗 Multi-Agent Automotive Report Generator")

car_name = st.text_input("Enter Car Name")

if st.button("Generate Report"):
    if car_name.strip() == "":
        st.warning("Please enter a car name.")
    else:
        try:
            response = requests.post(
                "http://127.0.0.1:8000/generate-report",
                json={"car_name": car_name},
            )

            if response.status_code == 200:
                report = response.json()["report"]
                st.success("Report Generated!")
                st.write(report)
            else:
                st.error("API Error")
        except Exception as e:
            st.error("Backend not running. Start FastAPI first.")
