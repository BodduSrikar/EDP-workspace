# 📰 Fake News Detector

An End-to-End Machine Learning System designed to detect, analyze, and classify news articles and headlines as **REAL** or **FAKE** using Natural Language Processing (NLP) techniques and supervised learning algorithms.

---

## 📌 Project Overview

With the rapid spread of digital information, fake news and misinformation pose a significant challenge. This project builds an automated classification engine that processes raw news text, extracts linguistic features, and applies statistical machine learning models to determine article credibility with high accuracy.

### Key Features
* **Data Cleaning & NLP Preprocessing:** Handles missing values, strips unwanted characters, lowercases, and removes noise from raw article text.
* **Feature Extraction:** Converts text data into high-dimensional numerical feature vectors using term frequency representations.
* **Supervised Classification:** Employs classification models (e.g., Logistic Regression) to deliver fast and reliable binary classification outputs (`0` for Real, `1` for Fake).
* **Evaluation & Metrics:** Rigorously validated using Accuracy, Precision, Recall, F1-Score, and Confusion Matrix metrics.
* **Modular Architecture:** Structured with dedicated frontend UI components, backend ML pipelines, and reusable source scripts.

---

## 📂 Project Architecture

```text
Fake-News-Detector/
│
├── backend/                             <-- Machine Learning & API Logic
│   ├── data/                            <-- Cleaned news datasets
│   ├── notebooks/                       <-- Jupyter Notebooks for analysis & training
│   ├── src/                             <-- Core python helper modules (preprocessing, training)
│   ├── models/                          <-- Saved trained model binaries (.pkl)
│   ├── main.py                          <-- Main application entry point
│   └── requirements.txt                 <-- Backend dependencies
│
├── frontend/                            <-- User Interface Components
│   ├── index.html                       <-- Web UI layout
│   ├── style.css                        <-- Custom styling
│   └── script.js                        <-- Client-side logic & API calls
│
├── .gitignore                           <-- Git exclusion configuration
└── README.md                            <-- Project documentation


🛠️ Tech Stack
Programming Language: Python 3.x

Data Manipulation & Analysis: Pandas, NumPy

Machine Learning & NLP: Scikit-Learn, NLTK

Model Serialization: Joblib

Frontend Interface: HTML5, CSS3, JavaScript 
