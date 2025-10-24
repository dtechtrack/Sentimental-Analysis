# Sentiment Analysis Project 📝

[![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)]()
[![Machine Learning](https://img.shields.io/badge/Machine%20Learning-F4B400?style=for-the-badge&logo=scikitlearn&logoColor=white)]()
[![NLP](https://img.shields.io/badge/NLP-00B8D9?style=for-the-badge&logo=python&logoColor=white)]()
[![SVM](https://img.shields.io/badge/SVM-FF6F61?style=for-the-badge&logo=python&logoColor=white)]()

---

## 🌟 Project Overview

This project focuses on **automatically determining the sentiment (positive or negative) of product reviews** using **Natural Language Processing (NLP)** and **Machine Learning**.  

The goal is to help businesses efficiently analyze large volumes of customer feedback from online reviews and classify them as **positive** or **negative**.

---

## 🛠️ Methods Used

The project uses a **machine learning-based approach** with the following steps:

1. **Text Preprocessing**
   - Lowercasing text
   - Tokenization (splitting text into words)
   - Stopword removal (`the`, `is`, `and`, etc.)
   - Punctuation removal
   - Lemmatization/Stemming (e.g., `running` → `run`)

2. **Feature Extraction**
   - Converts text into numerical format using **TF-IDF (Term Frequency–Inverse Document Frequency)**

3. **Model Training**
   - **Support Vector Machine (SVM)** as the primary algorithm
   - Hyperparameter tuning using **Grid Search** to optimize performance

4. **Model Evaluation**
   - Metrics used: **Accuracy, Precision, Recall, F1-Score, Confusion Matrix**

---

## ⚙️ How It Works

1. **Data Collection:** Gather product reviews from datasets.  
2. **Preprocessing:** Clean and standardize the text.  
3. **Feature Extraction:** Transform text into numerical features using TF-IDF.  
4. **Model Training:** Train SVM model using labeled training data.  
5. **Prediction & Evaluation:** Predict sentiment of new reviews and evaluate performance.

---

## 🤖 Algorithms & Classifiers

- **Support Vector Machine (SVM):** Primary classifier for text data  
- **Other Classifiers Evaluated:**
  - Naive Bayes  
  - Random Forest  
  - K-Means (unsupervised, used for comparison)  
  - Voting Classifier (ensemble of multiple classifiers)

---

## 📊 Accuracy & Performance

| Classifier          | Accuracy (%) |
|--------------------|-------------|
| SVM                | 85.63       |
| Naive Bayes        | 78.32       |
| Random Forest      | 81.15       |
| K-Means            | 65.40       |
| Voting Classifier  | 83.72       |

**Key Metrics:** Accuracy, Precision, Recall, F1-Score, Confusion Matrix

---

## 💪 Key Strengths

- **TF-IDF** effectively weighs words based on importance  
- **Hyperparameter tuning** improves SVM performance  
- **Comparison with multiple classifiers** provides benchmarks  

---

## ⚠️ Limitations & Future Work

- **Data Imbalance:** More positive reviews could bias results  
- **Ambiguity in Sentiment:** Sarcasm and mixed sentiments pose challenges  
- **Model Complexity:** SVM can be computationally intensive for large datasets  

**Future Work:**
- Explore **deep learning models** (RNNs, LSTMs)  
- Use **contextual embeddings** (BERT, GPT)  
- Address data imbalance using **SMOTE** or other techniques  

---

## 📁 Project Structure
SentimentApp/
├── data/ # Datasets
├── notebooks/ # Jupyter notebooks for exploration
├── src/ # Source code for preprocessing, feature extraction, training
├── models/ # Trained models
├── README.md # Project overview
└── requirements.txt # Dependencies


---

## 📌 Contact

For questions or collaboration, reach me at: **topiya.dhruvi@gmail.com**  

---

> 🚀 This project is a great example of combining **NLP**, **Machine Learning**, and **practical data science** to understand customer sentiment from text data!
