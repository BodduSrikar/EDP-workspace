import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from backend.src.preprocess import clean_text

def train_and_save_model():
    data_path = os.path.join("backend", "data", "cleaned_news_dataset.csv")
    
    if not os.path.exists(data_path):
        print(f"❌ Error: Dataset file not found at {data_path}")
        return

    print("⏳ Loading cleaned dataset...")
    df = pd.read_csv(data_path)
    df['text'] = df['text'].fillna('').apply(clean_text)

    X_train, X_test, y_train, y_test = train_test_split(
        df['text'], df['label'], test_size=0.20, random_state=42, stratify=df['label']
    )

    print("⏳ Vectorizing text using TF-IDF...")
    tfidf = TfidfVectorizer(max_features=10000, stop_words='english', ngram_range=(1, 2))
    X_train_vec = tfidf.fit_transform(X_train)
    X_test_vec = tfidf.transform(X_test)

    print("⏳ Training Logistic Regression model...")
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train_vec, y_train)

    accuracy = accuracy_score(y_test, model.predict(X_test_vec))
    print(f"✅ Training Complete! Model Accuracy: {accuracy * 100:.2f}%")

    model_dir = os.path.join("backend", "models")
    os.makedirs(model_dir, exist_ok=True)
    
    joblib.dump(model, os.path.join(model_dir, "fake_news_model.pkl"))
    joblib.dump(tfidf, os.path.join(model_dir, "vectorizer.pkl"))
    print(f"📦 Model and TF-IDF vectorizer saved in {model_dir}")

if __name__ == "__main__":
    train_and_save_model()