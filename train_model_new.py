import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Load the new CSV
df = pd.read_csv('phishing_data_new.csv')

# Remove any extra spaces from column names
df.columns = df.columns.str.strip()

# Split features and target
X = df.drop('Phishing', axis=1)
y = df['Phishing']

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Random Forest
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# Evaluate accuracy
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Save the trained model
joblib.dump(model, 'phishing_model.pkl')
print("Model saved as phishing_model.pkl")
