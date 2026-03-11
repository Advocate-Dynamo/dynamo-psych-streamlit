import streamlit as st
import pandas as pd

st.set_page_config(page_title="Advocate Dynamo", layout="wide")

st.title("Advocate Dynamo")
st.subheader("Between-visit behavioral monitoring")

st.warning(
"Prototype demonstration system. Not HIPAA compliant. Do not enter real medical information."
)

st.divider()

st.header("Patient Overview")

patients = ["Demo Patient A", "Demo Patient B", "Demo Patient C"]

selected_patient = st.selectbox(
"Select Patient",
patients
)

st.write("Selected patient:", selected_patient)

st.divider()

st.header("Trajectory")

demo_data = pd.DataFrame({
"Day": ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
"Mood": [3,4,2,3,5,4,3]
})

st.line_chart(demo_data, x="Day", y="Mood")

st.divider()

st.header("Clinical Flags")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Sleep Risk", "Moderate")

with col2:
    st.metric("Adherence", "Good")

with col3:
    st.metric("Mood Trend", "Stable")

st.divider()

st.header("AI Summary (Prototype)")

st.info(
"Patient shows moderate variability in mood with no acute deterioration. "
"Recommend continued monitoring and clinician review if trend persists."
)
