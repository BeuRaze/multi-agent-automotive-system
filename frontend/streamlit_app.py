import streamlit as st
import requests

# ==============================
# PAGE CONFIG
# ==============================
st.set_page_config(
    page_title="Automotive AI",
    layout="centered"
)

st.title("🚗 Multi-Agent Automotive Report Generator")

# ==============================
# BACKEND URL (LIVE RENDER API)
# ==============================
BACKEND_URL = "https://automotive-ai-backend.onrender.com/generate-report"

# ==============================
# USER INPUT
# ==============================
car_name = st.text_input("Enter Car Name")

# ==============================
# BUTTON ACTION
# ==============================
if st.button("Generate Report"):

    if car_name.strip() == "":
        st.warning("Please enter a car name.")
    else:
        try:
            with st.spinner("Generating report... (first request may take 30-60 seconds)"):
                response = requests.post(
                    BACKEND_URL,
                    json={"car_name": car_name},
                    timeout=120
                )

            if response.status_code == 200:
                data = response.json()
                report = data.get("report", "No report returned.")
                st.success("Report Generated Successfully!")
                st.write(report)

            else:
                st.error(f"API Error: {response.status_code}")
                st.write(response.text)

        except requests.exceptions.RequestException as e:
            st.error("Network error. Backend may be waking up or unreachable.")
            st.write(str(e))

        except Exception as e:
            st.error("Unexpected error occurred.")
            st.write(str(e))