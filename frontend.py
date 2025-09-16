import streamlit as st
import pandas as pd
import joblib
import re

# Load trained model
model = joblib.load('phishing_model.pkl')

# ------------------ Feature extraction ------------------
def extract_features(url):
    url_length = len(url)
    https = 1 if url.startswith("https") else 0
    subdomains = url.count('.') - 1
    has_at = 1 if '@' in url else 0
    has_hyphen = 1 if '-' in url else 0
    digits = sum(c.isdigit() for c in url)
    suspicious_words = ['login', 'secure', 'update', 'free', 'account', 'verify', 'bank']
    has_suspicious_word = 1 if any(word in url.lower() for word in suspicious_words) else 0
    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    has_ip = 1 if re.search(ip_pattern, url) else 0

    return pd.DataFrame([[url_length, https, subdomains, has_at, has_hyphen, digits, has_suspicious_word, has_ip]],
                        columns=['URL_Length','HTTPS','Subdomains','Has_@','Has_Hyphen','Digits','Suspicious_Word','Has_IP'])
# ------------------------------------------------------------

st.title("Phishing URL Detector 🚨")

url_input = st.text_input("Enter URL to check:")

if st.button("Check URL"):
    if url_input:
        features = extract_features(url_input)
        prediction = model.predict(features)[0]
        if prediction == 1:
            st.error("⚠️ Phishing URL detected!")
        else:
            st.success("✅ URL seems safe")
    else:
        st.warning("Please enter a URL")
