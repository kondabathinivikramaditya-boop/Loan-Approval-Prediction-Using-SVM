# Loan Approval Prediction Using Support Vector Machine (SVM)

## Project Overview

This project aims to predict whether a loan application will be approved using a Support Vector Machine (SVM) classification model.

The dataset contains information such as applicant income, loan amount, education, marital status, credit history, and property area. Data preprocessing has been completed, and the dataset is now ready for model training.

---

## Dataset

- Dataset: Loan Approval Prediction
- Total Records: 614
- Features: 13
- Target Variable: Loan_Status

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Jupyter Notebook

---

## Project Workflow (Completed)

### 1. Imported Required Libraries

Imported all required Python libraries for data analysis and machine learning.

### 2. Loaded the Dataset

Loaded the CSV dataset using Pandas.

### 3. Explored the Dataset

Performed basic data exploration using:

- `head()`
- `shape`
- `info()`
- `describe()`
- `isnull().sum()`

---

### 4. Data Cleaning

- Checked missing values.
- Filled missing values using appropriate methods.
- Verified that no missing values remained.

---

### 5. Data Preprocessing

Performed One-Hot Encoding using `pd.get_dummies()` for categorical features.

Encoded columns include:

- Gender
- Married
- Dependents
- Education
- Self_Employed
- Property_Area

The target variable (`Loan_Status`) was also converted into numerical values.

---

### 6. Feature Selection

Separated the dataset into:

- **Features (X)**
- **Target Variable (y)**

---

### 7. Train-Test Split

Split the dataset into:

- 80% Training Data
- 20% Testing Data

Output:

```
X_train : (491, 14)
X_test  : (123, 14)

y_train : (491,)
y_test  : (123,)
```

---

## Current Project Status

Completed:

- Data Loading
- Data Exploration
- Data Cleaning
- Data Preprocessing
- One-Hot Encoding
- Feature Selection
- Train-Test Split

Next Steps:

- Feature Scaling
- Train SVM Model
- Model Evaluation
- Confusion Matrix
- Classification Report
- Save Model using Joblib
- Build Streamlit Web App

---

## Repository Structure

```
Loan-Approval-Prediction-Using-SVM/
│
├── dataset/
│   └── Loan_approval.csv
│
├── loan_prediction_svm.ipynb
│
└── README.md
```

---

## Author

**Vikramaditya Kondabathini**

GitHub:
https://github.com/kondabathinivikramaditya-boop
