import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
from sklearn.linear_model import LogisticRegression
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, classification_report

# Define function to preprocess input data
def preprocess_input(data):
    # Extracting features
    X = data[["num_trans_per_hour", "amount", "oldbalanceOrg", "newbalanceOrig", "oldbalanceDest", "newbalanceDest"]]

    # Impute missing values with mean
    imputer = SimpleImputer(strategy='mean')
    X_imputed = imputer.fit_transform(X)

    return X_imputed

# Function to load data and train the Logistic Regression model
def train_model():
    # Load the data into a Pandas DataFrame
    #data = pd.read_csv('Online_Payment_Fraud_Detection/combined_data.csv')
    data = pd.read_csv('combined_data.csv')

    # Extracting features (X) and target variable (y)
    X = data[["num_trans_per_hour", "amount", "oldbalanceOrg", "newbalanceOrig", "oldbalanceDest", "newbalanceDest"]]
    y = data["isFraud"]

    # Impute missing values with mean
    imputer = SimpleImputer(strategy='mean')
    X_imputed = imputer.fit_transform(X)

    # Train Logistic Regression
    model_lr = LogisticRegression()
    model_lr.fit(X_imputed, y)

    # Making predictions
    y_pred = model_lr.predict(X_imputed)

    # Evaluating the model
    accuracy = accuracy_score(y, y_pred)
    print("Accuracy:", accuracy)

    # Classification report
    print("\nClassification Report:")
    print(classification_report(y, y_pred))

    return model_lr

# Function to make predictions
def predict_and_save(file_path, model):
    try:
        # Load the input CSV file
        input_data = pd.read_csv(file_path)

        # Preprocess the input data
        X_input = preprocess_input(input_data)

        # Making predictions
        input_data['isFraud_lr'] = model.predict(X_input)

        # Save fraud-flagged data to a new CSV file
        fraud_data = input_data[input_data['isFraud_lr'] == 1]
        fraud_data.to_csv('fraud_flagged_data.csv', index=False)

        messagebox.showinfo("Info", "Fraud-flagged data has been saved to 'fraud_flagged_data.csv'")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to open file dialog
def open_file_dialog(model):
    file_path = filedialog.askopenfilename(filetypes=[("CSV_files", "*.csv")])
    if file_path:
        predict_and_save(file_path, model)

# Create the main window
root = tk.Tk()
root.title("Fraud Detection")

# Train model when the application starts
model_lr = train_model()

# Create and place the button
button = tk.Button(root, text="Upload CSV and Predict Fraud", command=lambda: open_file_dialog(model_lr))
button.pack(pady=20)

# Run the application
root.mainloop()
