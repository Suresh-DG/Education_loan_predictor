# 🎓 Education Loan Predictor

A user-friendly web application that predicts whether a student's loan application will be approved or rejected. This tool uses key student and co-signer information to provide an estimated outcome, helping students and parents make informed financial decisions.

---

## ✨ Overview

This project aims to demystify the student loan approval process. By inputting details about academic performance, financials, and loan requirements, the application provides a quick, visual prediction of the loan outcome. The model is trained on a synthetic dataset designed to reflect the Indian financial and educational landscape.

### Key Features:
-   **Instant Predictions:** Get an immediate estimate of loan approval status.
-   **User-Friendly Interface:** Simple and intuitive web form built with Streamlit.
-   **Data-Driven:** Based on a Random Forest Classifier model trained on key financial and academic features.
-   **Informative:** Helps users understand the factors that might influence a lender's decision.

## 🎯 Why This Project?

-   **Reduces Uncertainty:** Many students and parents are unsure about their chances of securing a loan, causing significant stress.
-   **Saves Time:** Provides a preliminary check before undergoing the lengthy formal application process with banks.
-   **Educational Tool:** Highlights the key factors that financial institutions consider, such as academic merit, co-signer stability, and loan specifics.

## 🛠️ Tech Stack

-   **Backend & ML:** Python, Scikit-Learn
-   **Data Manipulation:** Pandas, NumPy
-   **Web Framework:** Streamlit
-   **Model Persistence:** Joblib

## 🔄 Workflow

1.  **Load Data:** The synthetic CSV dataset simulating student loan applications is loaded.
2.  **Feature Engineering:** New, insightful features are created:
    -   `Academic Status`
    -   `Co-signer Strength`
    -   `Loan Risk`
    -   `Relationship Strength`
3.  **Data Preprocessing:** Categorical features are converted into a machine-readable format using one-hot encoding.
4.  **Model Training:** A Random Forest Classifier is trained on the preprocessed data to learn the patterns for loan approval.
5.  **Model Serialization:** The trained model and feature columns are saved using Joblib for later use in the web app.
6.  **Web Interface:** A Streamlit application provides a simple interface for users to input their details and receive predictions.

## 📊 Dataset

The model is trained on a synthetic dataset created to simulate realistic student loan applications in India. The data ranges and distributions are based on publicly available information.

### Features
-   `CGPA` `Degree Level` `Course Duration` `Part-Time Income` `Scholarship Amount` `Co-signer Income` `Co-signer Credit History` `Relationship with Co-signer` `Loan Purpose` `Loan Amount Requested`
-   `Loan Status` (Target Variable)

### References / Sources
The synthetic data is modeled based on insights from:
RBI Reports on Student Loans, Loan products from SBI, HDFC Credila, Axis Bank, and ICICI Bank, UGC & AICTE Scholarship Schemes

## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine.

### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/Suresh-DG/Education_loan_predictor
    ```

2.  **Navigate to the project directory:**
    ```sh
    cd Education_loan_predictor
    ```

3.  **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

### Required Files
Ensure the following files are present in your project directory after cloning:
-   `main.py` (The Streamlit app script)
-   `loan_model.pkl` (The trained machine learning model)
-   `feature_cols.pkl` (The list of feature columns used for prediction)
-   `requirements.txt`

### Usage

1.  **Run the Streamlit application from your terminal:**
    ```sh
    streamlit run main.py
    ```

2.  **Open your web browser** and navigate to the local URL provided (usually `http://localhost:8501`).

3.  **Enter the student, co-signer, and loan details** into the web form.

4.  **Click the "Predict Loan Approval" button** to see the result.

5.  The prediction will be displayed on the screen as either **✅ Approved** or **❌ Rejected**, along with the model's confidence probability.

## ⚠️ Disclaimer

This tool is for educational and illustrative purposes only. The predictions are estimates and are not a guarantee of any actual loan outcome. Always consult with a financial advisor and the respective lending institutions for accurate information and decisions.
