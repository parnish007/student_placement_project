import sys
import os
import sys
import os

# Add project root (student_placement_project) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.predict import predict_student
import streamlit as st
import pandas as pd 

st.set_page_config(page_title="Student Placement Predictor", page_icon="🎓")
st.title("🎓 Student Placement Prediction App")
st.markdown(
    "Fill in the student's details below and click **Predict Placement** to see the result."
)

# Two-column layout
col1, col2 = st.columns(2)

with col1:
    IQ = st.number_input("IQ", min_value=41, max_value=158, value=99)
    Prev_Sem_Result = st.number_input(
        "Previous Semester Result", min_value=5.0, max_value=10.0, value=7.54, step=0.01
    )
    CGPA = st.number_input("CGPA", min_value=4.54, max_value=10.46, value=7.53, step=0.01)
    Academic_Performance = st.number_input(
        "Academic Performance Score", min_value=1, max_value=10, value=6
    )

with col2:
    Extra_Curricular_Score = st.number_input(
        "Extra Curricular Score", min_value=0, max_value=10, value=5
    )
    Communication_Skills = st.number_input(
        "Communication Skills Score", min_value=1, max_value=10, value=6
    )
    Projects_Completed = st.number_input(
        "Projects Completed", min_value=0, max_value=5, value=3
    )
    Internship_Experience = st.selectbox("Internship Experience", options=["Yes", "No"])

# Prepare input dictionary
student_data = {
    'IQ': IQ,
    'Prev_Sem_Result': Prev_Sem_Result,
    'CGPA': CGPA,
    'Academic_Performance': Academic_Performance,
    'Extra_Curricular_Score': Extra_Curricular_Score,
    'Communication_Skills': Communication_Skills,
    'Projects_Completed': Projects_Completed,
    'Internship_Experience': str(Internship_Experience),  # ensure string
}

# Predict button
if st.button("Predict Placement"):
    try:
        result = predict_student(student_data)
        prediction = result.get('prediction', "No result")
        probability = result.get('probability', None)

        # Display prediction
        if prediction == "Yes":
            st.success("🎯 Congratulations! The student is likely to be **PLACED**.")
        elif prediction == "No":
            st.error("❌ Unfortunately, the student is likely **NOT PLACED**. Keep improving!")
        else:
            st.warning(f"⚠️ Unexpected prediction: {prediction}")

        # Display probability as a progress bar if available
        if probability is not None:
            not_placed_prob = probability[0]
            placed_prob = probability[1]

            st.subheader("📊 Placement Probabilities")
            st.progress(int(placed_prob * 100))
            st.write(f"✅ Placed: {placed_prob*100:.2f}%")
            st.write(f"❌ Not Placed: {not_placed_prob*100:.2f}%")

    except Exception as e:
        st.error(f"⚠️ Error during prediction. Please check input values.\nDetails: {e}")
