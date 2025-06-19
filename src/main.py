import openai
import csv
import firebase_admin
from firebase_admin import credentials, db

# Set up Firebase only ONCE
cred = credentials.Certificate("")  # Replace with your Firebase JSON key
firebase_admin.initialize_app(cred, {
    "databaseURL": ""  # Replace with your database URL
})

# OpenAI API Key
openai.api_key = ''  # Replace with your actual API key

categorized_tweet = ["Sports", "Politics", "Technology", "International News","Weather", "Others"]

def classify_tweet(tweet, categories=categorized_tweet):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Classify the given tweet ({tweet}) into one of these categories: {categories}. Only return the category name, no extra text."}
        ],
        max_tokens=10
    )
    return response.choices[0]["message"]["content"].strip()

def generate_heading(tweet):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Generate a short, catchy heading for this tweet: {tweet}"}
        ],
        max_tokens=20
    )
    return response.choices[0]["message"]["content"].strip()

def generate_analysis(category, tweets):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Analyze and review these tweets under the category '{category}' to identify key insights and trends. Provide a professional and well-structured analysis, incorporating broader context and relevant knowledge. Go beyond the tweets to explain underlying themes, possible implications, and any noteworthy patterns. Ensure clarity, accuracy, and a logical flow in the analysis in 50 to 60 words and in descriptive way and human style{tweets}"}
        ],
        max_tokens=200
    )
    return response.choices[0]["message"]["content"].strip()

def classify_tweets_from_csv(file_path):
    with open(file_path, mode='r', encoding='ISO-8859-1') as file:
        reader = csv.reader(file)
        next(reader)
        classified_tweets = []
        categorized_tweets = {category: [] for category in categorized_tweet}

        for row in reader:
            tweet = row[0]
            related_class = classify_tweet(tweet)

            # Ensure the classified category exists in the predefined categories
            if related_class not in categorized_tweet:
                related_class = "Others"  # Default category for unexpected classifications

            heading = generate_heading(tweet)
            classified_tweets.append((tweet, related_class, heading))
            categorized_tweets.setdefault(related_class, []).append(tweet)  # Avoid KeyError

    return classified_tweets, categorized_tweets

# 🔹 Firebase Upload Function
def upload_to_firebase(classified_tweets, categorized_tweets):
    # Upload classified tweets with headings
    db_ref = db.reference("/tweet_analysis/2025-02-11_heading/Headings")
    for tweet, related_class, heading in classified_tweets:
        db_ref.push({
            "heading": heading,
            "tweet": tweet,
            "class": related_class
        })

    # Upload analysis for each category
    analysis_ref = db.reference("/tweet_analysis/2025-02-11_analysis/Analysis")
    for category, tweets in categorized_tweets.items():
        if tweets:
            analysis = generate_analysis(category, tweets)
            analysis_ref.child(category).set({
                "analysis": analysis,
                "tweets": tweets
            })

if __name__ == "__main__":
    file_path = 'tweets.csv'
    classified_tweets, categorized_tweets = classify_tweets_from_csv(file_path)

    # Print classified tweets with headings
    for tweet, related_class, heading in classified_tweets:
        print(f"Heading: {heading}\nTweet: {tweet}\nClass: {related_class}\n")

    # Generate and print analysis for each category
    for category, tweets in categorized_tweets.items():
        if tweets:
            analysis = generate_analysis(category, tweets)
            print(f"### Analysis for {category} ###\n{analysis}\n")

    # 🔹 Call Firebase upload function (Only Once)
    upload_to_firebase(classified_tweets, categorized_tweets)
    print("✅ Data successfully uploaded to Firebase!")
