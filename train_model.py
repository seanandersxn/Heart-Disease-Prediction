import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import joblib

# Database Connection
conn = sqlite3.connect('heartDisease.db')

# Load Data from SQLite Database
cleanedData = pd.read_sql_query("SELECT * FROM heartDiseaseCleanedData", conn)
conn.close()

# Define categorical and numeric variables
categoricalVariables = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal']
numericVariables = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']

# Split the Data into Features (x) and the target (y)
X = cleanedData.drop(columns=['target'])
y = cleanedData['target']

# Preprocess the Categorical Variables
label_encoder = LabelEncoder()
for column in categoricalVariables:
    X[column] = label_encoder.fit_transform(X[column])

# Split the Data into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale Numberic Variables
scaler = StandardScaler()
X_train[numericVariables] = scaler.fit_transform(X_train[numericVariables])
X_test[numericVariables] = scaler.transform(X_test[numericVariables])

# Define Models to be Evaluated
models = {
    "Logistic Regression": LogisticRegression(),
    "Random Forest": RandomForestClassifier(),
    "Support Vector Classsifer": SVC()
}

# Train and Evaluate the Models
bestModel = None
bestAccuracy = 0

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred) * 100
    print(f"{name} Accuracy: {accuracy:.2f}%")
    if accuracy > bestAccuracy:
        bestAccuracy = accuracy
        bestModel = model

# Save the Best Model and Scaler to Disk.
if bestModel:
    joblib.dump(bestModel, 'best_model.pkl')
    joblib.dump(scaler, 'scaler.pkl') 
    print(f"The best model ({type(bestModel).__name__}) has been saved to 'best_model.pkl'")
else:
    print("No best model has been found or trained.")