import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix

def load_and_preprocess_data(filepath):
    print("Loading customer churn dataset...")
    df = pd.read_csv(filepath)
    
    # Handle missing values
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df['TotalCharges'].fillna(df['TotalCharges'].median(), inplace=True)
    
    # Binary encoding
    df['Churn'] = df['Churn'].apply(lambda x: 1 if x == 'Yes' else 0)
    
    # One-hot encoding for categorical variables
    categorical_cols = ['gender', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines',
                        'InternetService', 'OnlineSecurity', 'Contract', 'PaymentMethod']
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
    
    # Drop identifier columns
    X = df.drop(columns=['customerID', 'Churn'])
    y = df['Churn']
    
    return X, y

def train_churn_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    print("Training RandomForest Classifier...")
    model = RandomForestClassifier(n_estimators=100, max_depth=8, random_state=42)
    model.fit(X_train_scaled, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test_scaled)
    y_probs = model.predict_proba(X_test_scaled)[:, 1]
    
    print("\nModel Evaluation:")
    print(classification_report(y_test, y_pred))
    print(f"ROC AUC Score: {roc_auc_score(y_test, y_probs):.4f}")
    
    return model, scaler

if __name__ == "__main__":
    # Simulate run
    print("Customer Churn Prediction pipeline initialized successfully.")
