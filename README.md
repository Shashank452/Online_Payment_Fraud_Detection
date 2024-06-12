# Online_Payment_Fraud_Detection

# Abstract: Online Payment Fraud Detection using Logistic Regression
As online payment methods become increasingly popular, the risk of fraud also rises. Detecting fraudulent transactions is crucial to maintaining trust and security in digital financial systems. In this context, machine learning techniques play a vital role.

In our study, we focus on using logistic regression for fraud detection in payment transactions. We leverage labeled datasets containing payment records to train and evaluate our model. Specifically:

Problem Statement: We address the challenge of identifying fraudulent transactions within a given dataset.

Methodology:
We apply logistic regression, a widely used classification algorithm, to predict whether a transaction is fraudulent (class 1) or legitimate (class 0).
Our model learns from features such as transaction type, amount, sender’s balance, and receiver’s balance.

Results:
Our proposed approach achieves high accuracy in detecting fraud transactions.
We strike a balance by minimizing false positives (legitimate transactions incorrectly flagged as fraud).

Conclusion:
Logistic regression, when properly tuned, provides an effective solution for online payment fraud detection.
Future work may explore ensemble methods or other advanced techniques to further enhance performance.
This abstract highlights the significance of logistic regression in combating online payment fraud. 

# Algorithms used for Online_Payment_Fraud_Detection

1) Logistic Regression (LR):
Purpose: Logistic regression is a widely used classification algorithm for binary and multiclass problems.

How It Works:
Given input features (e.g., transaction details), logistic regression estimates the probability of an instance belonging to a specific class (e.g., fraud or non-fraud).

It models the log-odds (logit) of the probability as a linear combination of input features.
The logistic function (sigmoid) maps the log-odds to a probability between 0 and 1.

Advantages:

Simplicity and interpretability.
Works well when the relationship between features and the target is approximately linear.

Limitations:
Assumes that the decision boundary is linear.
Sensitive to outliers.

In the Code:
The LogisticRegression class from scikit-learn is used to train a logistic regression model.
The model is trained on features related to transaction details (e.g., num_trans_per_hour, amount, balances).
Predictions are made using the trained model, and accuracy and classification report metrics are evaluated.

2) Data Preprocessing:
Purpose: Prepare the data for modeling.

Steps:
Extract relevant features (columns) from the dataset.
Impute missing values (using mean imputation in this case).
Split the data into features (X) and the target variable (y).

3) Application Flow:
The code defines functions for preprocessing input data, training the logistic regression model, making predictions, and saving results.

It creates a simple GUI application using tkinter, allowing users to upload a CSV file and predict fraud.
When the user uploads a file, the model predicts whether each transaction is fraudulent or not.
Fraud-flagged data is saved to a new CSV file.

5) Evaluation:
The accuracy of the model is calculated using the ground truth labels.

The classification report provides additional metrics such as precision, recall, and F1-score.

# Below are the steps to run the provided code for online payment fraud detection using logistic regression:

1) Install Required Packages:
Make sure you have Python installed on your system.
Create a virtual environment (optional but recommended).

Install the required packages using:
pip install -r requirements.txt

2) Prepare Your Data:
Ensure you have a CSV file containing payment transaction data (similar to the provided combined_data.csv).

The file should have columns like num_trans_per_hour, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, and newbalanceDest.

4) Run the Code:
Save the provided code snippet to a Python file (e.g., fraud_detection.py).

Replace 'combined_data.csv' with the actual path to your dataset in the code.

Open a terminal or command prompt and navigate to the directory containing your Python file.

Run the script using:
python solution.py

6) GUI Application:
A window will open with a button labeled “Upload CSV and Predict Fraud.”

Click the button and select your input CSV file "test.csv".

The model will predict fraud for each transaction and save fraud-flagged data to a new CSV file (fraud_flagged_data.csv).

8) View Results:
Check the terminal/command prompt for accuracy and classification report metrics.

Open the saved fraud_flagged_data.csv file to see the flagged transactions.
