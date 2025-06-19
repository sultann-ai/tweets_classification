# 🐦 Twitter Sentiment Classifier using OpenAI API

This project fetches tweets using the Twitter API and classifies their sentiment (Positive, Negative, Neutral) using the OpenAI GPT API — no traditional machine learning model is used. The results are displayed on a Flask-powered website and stored in Firebase Realtime Database.

---

## 📌 Project Overview

- 🔄 Tweets are fetched using the Twitter API based on a keyword or username.
- 🤖 Tweets are sent to OpenAI's GPT API for prompt-based sentiment classification.
- 💡 GPT returns the sentiment as Positive, Negative, or Neutral.
- 🌐 A Flask web app displays the tweet sentiments in real time.
- ☁️ All results are stored and synced with Firebase Realtime Database.

---

## 🧰 Tech Stack

- **Backend**: Python, Flask
- **APIs**: OpenAI GPT API, Twitter API v2
- **Database**: Firebase Realtime Database
- **Frontend**: HTML, CSS, Jinja2 (Flask Templates)
- **Other**: Pandas, JSON, Requests

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/twitter-sentiment-classifier.git
cd twitter-sentiment-classifier
