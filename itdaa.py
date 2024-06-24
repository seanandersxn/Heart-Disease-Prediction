import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create a Database Connection
db_name = 'heartDisease.db'
conn = sqlite3.connect(db_name)

# Read the CSV File with a Semicolon Delimiter
csv_file = r'heart.csv'
data = pd.read_csv(csv_file, delimiter=';')

# Cleaning and Preprocessing
# Handle any Missing Values
data = data.dropna()

# Convert Categorical Variables
categorical_variables = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal']
for column in categorical_variables:
    data[column] = data[column].astype('category')

# Convert Target Variable
data['target'] = data['target'].astype('category')

# Upload the Cleaned Data to the Data Frame
table_name = 'heartDiseaseCleanedData'
data.to_sql(table_name, conn, if_exists='replace', index=False)

# Verify the Upload
cursor = conn.cursor()
cursor.execute(f"SELECT * FROM {table_name} LIMIT 5")
rows = cursor.fetchall()

# Close the Connection
conn.close()

# Plotting the Distribution of Categorical Variables
fig, axes = plt.subplots(nrows=4, ncols=2, figsize=(15, 10))
axes = axes.flatten()
for i, column in enumerate(categorical_variables):
    sns.countplot(data=data, x=column, hue='target', ax=axes[i])
    axes[i].set_title(f'Distribution of {column} by Target Variable')
    axes[i].set_xlabel(column)
    axes[i].set_ylabel('Count')
    handles, labels = axes[i].get_legend_handles_labels()
    axes[i].legend(handles, labels, title='target')

# Adjust Layout Height to Prevent Overlapping
plt.tight_layout(h_pad=1.0)

# Plotting the Distribution of Numeric Variables
numeric_variables = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']  # Replace with actual numeric variable names

fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(15, 12))
axes = axes.flatten()
for i, column in enumerate(numeric_variables):
    sns.histplot(data=data, x=column, hue='target', multiple='stack', kde=True, ax=axes[i])
    axes[i].set_title(f'Distribution of {column} by Target Variable')
    axes[i].set_xlabel(column)
    axes[i].set_ylabel('Count')
    handles, labels = axes[i].get_legend_handles_labels()
    axes[i].legend(handles, labels, title='target')

plt.tight_layout()
plt.show()