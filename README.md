# Heart Disease Prediction
This Heart Disease Prediction application uses machine learning to assess a patient's likelihood of having heart disease based on key health metrics. The app features a user-friendly interface powered by Streamlit, where users input health data to receive instant predictions.

# 🚀 Features
* Machine Learning-Based Prediction – Uses a trained model to evaluate heart disease risk.
* Interactive UI – Built with Streamlit for seamless user experience.
* Data Preprocessing & Visualization – Handles data cleaning, feature scaling, and exploratory analysis.
* Model Training & Evaluation – Compares multiple classifiers (Logistic Regression, Random Forest, SVM) to select the best-performing model.
* SQLite Database Integration – Stores and processes heart disease datasets.

# 🏗️ Tech Stack
* Python (Data Processing & ML)
* Streamlit (Web App)
* Scikit-learn (Model Training)
* Joblib (Model Persistence)
* Pandas & NumPy (Data Handling)
* Matplotlib & Seaborn (Data Visualization)
* SQLite (Database)

# 📂 Project Structure
* app.py – Streamlit-based web interface for user input and prediction.
* itdaa.py – Data preprocessing, visualization, and storage in SQLite.
* trainmodel.py – ML model training, evaluation, and selection of the best model.

# 🔧 How to Run
Clone the repository:

git clone https://github.com/seanandersxn/Heart-Disease-Prediction.git  
cd Heart-Disease-Prediction  

Install dependencies:
pip install -r requirements.txt  

Train the model (if not already trained):
python trainmodel.py  

Run the app:
streamlit run app.py  

# 📌 Disclaimer
This application is for educational and informational purposes only. It does not replace professional medical advice. Consult a healthcare professional for accurate diagnosis and treatment.
