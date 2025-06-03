import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
def train_model():
    np.random.seed(42)
    num_students = 200

    data = {
        'attendance_rate': np.random.uniform(0.5, 1.0, num_students),
        'average_grade': np.random.uniform(40, 100, num_students),
        'study_hours_per_week': np.random.randint(1, 30, num_students),
        'assignments_completed': np.random.randint(5, 11, num_students)
    }

    df = pd.DataFrame(data)
    df['at_risk'] = ((df['attendance_rate'] < 0.75) &
                     (df['average_grade'] < 60) &
                     (df['study_hours_per_week'] < 10)).astype(int)

    X = df.drop('at_risk', axis=1)
    y = df['at_risk']
    model = RandomForestClassifier(random_state=42)
    model.fit(X, y)
    return model


model = train_model()

st.title("🎓 Student Risk Prediction")
st.markdown("Enter student performance details to predict if they are at risk.")

attendance = st.slider("Attendance Rate", 0.0, 1.0, 0.9, 0.01)
grade = st.slider("Average Grade", 0, 100, 75)
study_hours = st.slider("Study Hours per Week", 0, 40, 10)
assignments = st.slider("Assignments Completed (out of 10)", 0, 10, 8)

if st.button("Predict Risk"):
    input_data = np.array([[attendance, grade, study_hours, assignments]])
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠️ The student is at risk.")
    else:
        st.success("✅ The student is not at risk.")
