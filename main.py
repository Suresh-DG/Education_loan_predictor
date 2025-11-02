import streamlit as st
import pandas as pd
import numpy as np
import joblib
model = joblib.load("loan_model.pkl")
scaler = joblib.load("scaler.pkl")
feature_cols = joblib.load("feature_cols.pkl")
def prepare_input(data):
    df = pd.DataFrame([data])
    df['Academic_Status'] = np.where(df['CGPA'] >= 7.0, 1, 0)
    df['CoSigner_Financial_Strength'] = np.where((df['CoSigner_Income'] >= 25000) | (df['CoSigner_Credit_History'] == 1), 1, 0)
    df['Loan_Amount_Risk'] = np.where(df['LoanAmount'] <= 500000, 0, 1)
    df['Relationship_Strength'] = df['Relationship_With_CoSigner'].map({'Parent': 2, 'Guardian': 2, 'Relative': 1, 'Sibling': 1})
    df['Has_Bonus_Points'] = np.where((df['Scholarship_Amount'] > 0) | (df['Part_Time_Income'] > 0), 1, 0)
    df['Course_Duration_Status'] = np.where(df['Course_Duration_Years'] <= 5, 1, 0)
    df['Income_Loan_Ratio'] = df['CoSigner_Income'] / (df['LoanAmount'] + 1)
    df['Scholarship_Coverage'] = df['Scholarship_Amount'] / (df['LoanAmount'] + 1)
    df['Total_Student_Income'] = df['Part_Time_Income'] + df['Scholarship_Amount']
    df['Financial_Support_Score'] = (df['CoSigner_Credit_History'] * 0.3 + df['Academic_Status'] * 0.3 + df['Has_Job_Offer'] * 0.2 + df['Has_Bonus_Points'] * 0.2)
    df = pd.get_dummies(df, drop_first=True)
    df = df.reindex(columns=feature_cols, fill_value=0)
    return df
st.title("Education Loan Predictor")
degree_level = st.selectbox("Degree Level", ["UG", "M.Tech", "MBA"])
cgpa = st.slider("CGPA", 0.0, 10.0, 8.0)
course_duration = st.number_input("Course Duration (Years)", 1, 10, 4)
part_time_income = st.number_input("Part-Time Income", 0, 100000, 5000)
scholarship = st.number_input("Scholarship Amount", 0, 1000000, 10000)
has_job_offer = st.radio("Has Job Offer?", ["Yes", "No"])
cosigner_income = st.number_input("Co-signer Income", 0, 1000000, 30000)
cosigner_credit = st.radio("Co-signer has Credit History?", ["Yes", "No"])
relationship_cosigner = st.selectbox("Relationship with Co-signer", ["Parent", "Guardian", "Relative", "Sibling"])
field_of_study = st.selectbox("Field of Study", ["Computer Applications", "Mechanical Engineering", "MBA (Finance)", "MBA (HR)", "MBA (Marketing)"])
loan_purpose = st.selectbox("Loan Purpose", ["Tuition", "Living Expenses"])
loan_amount = st.number_input("Loan Amount Requested", 10000, 1000000, 400000)
if st.button("Predict Loan Approval"):
    applicant = {
        "Degree_Level": degree_level, "CGPA": cgpa, "Course_Duration_Years": course_duration, "Part_Time_Income": part_time_income, "Scholarship_Amount": scholarship,
        "Has_Job_Offer": 1 if has_job_offer == "Yes" else 0, "CoSigner_Income": cosigner_income, "CoSigner_Credit_History": 1 if cosigner_credit == "Yes" else 0, 
        "Relationship_With_CoSigner": relationship_cosigner, "Field_of_Study": field_of_study, "Loan_Purpose": loan_purpose,"LoanAmount": loan_amount}
    input_df = prepare_input(applicant)
    input_scaled = scaler.transform(input_df)
    pred = model.predict(input_scaled)[0]
    prob = model.predict_proba(input_scaled)[0][1] * 100
    if pred == 1:
        st.success(f"Loan Approved! Probability: {prob:.2f}%")
    else:
        st.error(f"Loan Rejected. Probability: {prob:.2f}%")