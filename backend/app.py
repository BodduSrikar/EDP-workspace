import os
import sys
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

# Add project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from backend.src.preprocess import clean_text

app = Flask(__name__)
CORS(app)  # Enables cross-origin requests from frontend HTML

base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, "models", "fake_news_model.pkl")
vectorizer_path = os.path.join(base_dir, "models", "vectorizer.pkl")

# Load model binaries
model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    headline = data.get('text', '')
    
    if not headline or not headline.strip():
        return jsonify({'error': 'No text provided'}), 400
        
    cleaned_input = clean_text(headline)
    vec_input = vectorizer.transform([cleaned_input])
    
    # Check if any word in the user's input exists in the model's 5,000-word vocabulary
    if vec_input.nnz == 0:
        return jsonify({'result': 'UNCERTAIN ⚠️ (Input text contains no recognized keywords from training data)'})
    
    prediction = model.predict(vec_input)[0]
    result = "FAKE" if prediction == 1 else "REAL"
    
    return jsonify({'result': result})