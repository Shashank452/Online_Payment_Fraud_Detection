# **Online Payment Fraud Detection**

This project uses machine learning to detect fraudulent online payment transactions. It utilizes a Logistic Regression model to classify transactions as either fraudulent or legitimate based on transaction details. The application provides a graphical interface using Tkinter, allowing users to upload a CSV file and predict whether the transactions in the file are fraudulent.

---

## **Features**
- **Fraud Detection**: Classifies transactions as fraudulent or legitimate using Logistic Regression.
- **Data Preprocessing**: Handles missing values by imputing with the mean and selecting relevant features for classification.
- **Graphical User Interface (GUI)**: A simple Tkinter-based GUI to allow users to upload CSV files for prediction.
- **Result Storage**: Saves fraud-flagged transactions in a new CSV file (`fraud_flagged_data.csv`).

---

## **Technologies Used**
- **Python**: Programming language for the project.
- **Pandas**: For data manipulation and processing.
- **Scikit-Learn**: For machine learning and model training (Logistic Regression).
- **Tkinter**: For creating the graphical user interface.
- **Matplotlib**: (Optional) For visualizing the model's performance (not included in this code but can be added).

---

## **Setup and Installation**

### **1. Clone the Repository**
Clone the repository to your local machine:
```bash
git clone https://github.com/Shashank452/Online_Payment_Fraud_Detection.git
cd Online_Payment_Fraud_Detection
```

### **2. Install Dependencies**
Install the required Python libraries using the requirements.txt file:
```bash
pip install -r requirements.txt
```

### **3. Required Files**
Make sure you have a CSV file (combined_data.csv) for model training and predictions. The dataset should contain the following columns:

- num_trans_per_hour: Number of transactions per hour.
- amount: Transaction amount.
- oldbalanceOrg: Previous balance of the sender.
- newbalanceOrig: New balance after transaction (sender).
- oldbalanceDest: Previous balance of the receiver.
- newbalanceDest: New balance after transaction (receiver).
- isFraud: Target variable indicating whether the transaction is fraudulent (1 for fraud, 0 for legitimate).

---

## **How to Run**
1. Train the Logistic Regression model by running the script:
```bash
python fraud_detection.py
```
2. The model will be trained, and the GUI will appear.
3. Click the "Upload CSV and Predict Fraud" button in the GUI to open a file dialog.
4. Select the CSV file containing the transactions you want to predict.
5. The application will process the file, make predictions, and save fraud-flagged transactions to fraud_flagged_data.csv.

---

## **Project Structure**
```markdown
online-payment-fraud-detection/
│
├── solution.py               # Main script for fraud detection and GUI
├── combined_data.csv         # Sample data for model training (must be provided)
├── fraud_flagged_data.csv    # Output file with fraud-flagged transactions
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

---

## **Future Enhancements**
- Implement additional machine learning models (e.g., Random Forest, SVM) for better performance.
- Integrate more features such as time of day, location, and device used.
- Improve the GUI with more options for user interaction and data visualization.

---

## **Contact**
If you have any questions or suggestions, feel free to reach out:
- **Author**: [Shashanka C K](mailto:your-email@example.com)  
- **GitHub**: [Shashank452](https://github.com/Shashank452)  
- **LinkedIn**: [Shashanka C K](https://www.linkedin.com/in/shashanka-c-k)
