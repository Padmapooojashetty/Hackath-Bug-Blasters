import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# ---------------- Step 1: Load CSV ----------------
# Tab-separated CSV
df = pd.read_csv('phishing_data_new.csv', sep='\t')

# Remove extra spaces in column names
df.columns = df.columns.str.strip()

# ---------------- Step 2: Split features and target ----------------
# Drop URL (text) and keep numeric features only
X = df.drop(['URL', 'Phishing'], axis=1)
y = df['Phishing']

# ---------------- Step 3: Split into train/test sets ----------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------------- Step 4: Train Random Forest ----------------
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# ---------------- Step 5: Evaluate ----------------
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# ---------------- Step 6: Save the model ----------------
joblib.dump(model, 'phishing_model.pkl')
print("Model saved as phishing_model.pkl")
