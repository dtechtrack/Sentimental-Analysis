import streamlit as st
import pickle
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

try:
    stop_words = stopwords.words('english')
except LookupError:
    nltk.download('stopwords')
    stop_words = stopwords.words('english')
    
# Load model and vectorizer
model = pickle.load(open("svm_model.pkl", "rb"))
vectorizer = pickle.load(open("tfidf_vectorizer.pkl", "rb"))

# Text cleaning function
def preprocess_text(text):
    ps = PorterStemmer()
    all_stopwords = stopwords.words('english')
    all_stopwords.remove('not')

    review = re.sub('[^a-zA-Z]', ' ', text)
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if word not in all_stopwords]
    review = ' '.join(review)
    return review

# Streamlit UI
st.title("📊 Sentiment Analysis of Product Reviews")

user_input = st.text_area("Enter your review here:")

if st.button("Analyze Sentiment"):
    cleaned = preprocess_text(user_input)
    vect = vectorizer.transform([cleaned]).toarray()
    prediction = model.predict(vect)[0]

    sentiment = "Positive" if prediction == 1 else "Negative" if prediction == 0 else "Neutral"
    st.write(f"### Sentiment: {sentiment}")
