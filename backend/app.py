import os
import sys
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import joblib


ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ROOT_DIR)

from backend.src.preprocess import clean_text


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "frontend"))
MODEL_PATH = os.path.join(BASE_DIR, "models", "fake_news_model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "models", "vectorizer.pkl")

app = Flask(__name__, static_folder=FRONTEND_DIR)
CORS(app)

print(" Loading model binaries...")
if not os.path.exists(MODEL_PATH) or not os.path.exists(VECTORIZER_PATH):
    print(" Model or vectorizer not found! Please run training first.")
    sys.exit(1)

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)
print(" Model and TF-IDF vectorizer successfully loaded!")

@app.route('/')
def serve_index():
    return send_from_directory(FRONTEND_DIR, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(FRONTEND_DIR, path)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json() or {}
    headline = data.get('text', '')
    
    if not headline or not headline.strip():
        return jsonify({'error': 'No text provided'}), 400
        
    cleaned_input = clean_text(headline)
    vec_input = vectorizer.transform([cleaned_input])
    
    # Check for empty out-of-vocabulary inputs
    if vec_input.nnz == 0:
        return jsonify({
            'result': 'UNCERTAIN',
            'confidence': 50.0,
            'message': 'Input text contains no recognized vocabulary from the training dataset.'
        })
    
    # Prediction and probabilities
    prediction = model.predict(vec_input)[0]
    probabilities = model.predict_proba(vec_input)[0]
    
    result = "FAKE" if prediction == 1 else "REAL"
    confidence = round(float(probabilities[prediction]) * 100, 2)
    
    return jsonify({
        'result': result,
        'confidence': confidence
    })

if __name__ == '__main__':
    print(" Flask API Server running at http://127.0.0.1:5000")
    app.run(host='127.0.0.1', port=5000, debug=False)