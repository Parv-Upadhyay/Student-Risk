# Student-Risk
This project is a Student Risk Prediction System built using Python and Streamlit. Its purpose is to determine whether a student is at risk of failing or dropping out, based on a few key performance indicators.

The system works by first simulating a dataset of students. Each student has data like attendance rate, average grades, study hours per week, and the number of assignments completed. Using simple rules, the system labels students as "at risk" if their performance falls below certain thresholds.

Next, a machine learning model—specifically, a Random Forest Classifier—is trained on this data. This model learns the patterns that typically indicate a student might be struggling.

Then, we use Streamlit to build an interactive web interface. This interface allows users—such as teachers or administrators—to input a student’s data using sliders. Once the data is entered, the model predicts whether the student is at risk. If they are, the system shows a warning; if not, it gives a green check.

Overall, the project demonstrates how machine learning and user-friendly interfaces can be combined to help educational institutions identify and support students early, using data-driven insights.
