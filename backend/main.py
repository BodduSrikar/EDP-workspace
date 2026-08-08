import os
import sys

# Add project root directory to sys.path so 'backend' module is recognized
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import joblib
from backend.src.preprocess import clean_text

def predict_news(headline: str):
    # Locate models relative to this script's directory
    base_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(base_dir, "models", "fake_news_model.pkl")
    vectorizer_path = os.path.join(base_dir, "models", "vectorizer.pkl")

    if not os.path.exists(model_path) or not os.path.exists(vectorizer_path):
        print(" Saved model binaries not found. Run 'python -m backend.src.train' first.")
        return

    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)

    cleaned_input = clean_text(headline)
    vec_input = vectorizer.transform([cleaned_input])

    prediction = model.predict(vec_input)[0]
    result = "FAKE " if prediction == 1 else "REAL "
    
    print("\n--- Detection Result ---")
    print(f"Article Class: {result}")
    print("------------------------\n")

if __name__ == "__main__":
    text_input = input("Enter news text or headline to analyze:\n> ")
    if text_input.strip():
        predict_news(text_input)