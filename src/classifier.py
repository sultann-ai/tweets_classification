import csv
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Load the CSV file
tweets = []
with open('C:/Users/Hp/OneDrive/Desktop/icat/tweets.csv', newline='', encoding='utf-8') as csvfile:
    tweet_reader = csv.DictReader(csvfile)
    for row in tweet_reader:
        tweets.append({"tweetText": row["tweetText"], "username": row["username"]})

# Load the DistilBERT model
classifier = pipeline('text-classification', model='distilbert-base-uncased-finetuned-sst-2-english')

# Classify tweets using the new model
# Load model directly

tokenizer = AutoTokenizer.from_pretrained("distilbert/distilbert-base-uncased-finetuned-sst-2-english")
model = AutoModelForSequenceClassification.from_pretrained("distilbert/distilbert-base-uncased-finetuned-sst-2-english")

categorized_tweets = {
    "sportsTweets": [],
    "newsTweets": [],
    "technologyTweets": [],
    "healthTweets": [],
    "fashionTweets": []
}

for tweet in tweets:
    result = classifier(tweet["tweetText"])[0]
    print("result: ", result)
    label = result['label']
    if label == 'LABEL_0':  # Assuming LABEL_0 corresponds to sports
        categorized_tweets["sportsTweets"].append(tweet)
    elif label == 'LABEL_1':  # Assuming LABEL_1 corresponds to news
        categorized_tweets["newsTweets"].append(tweet)
    elif label == 'LABEL_2':  # Assuming LABEL_2 corresponds to technology
        categorized_tweets["technologyTweets"].append(tweet)
    elif label == 'LABEL_3':  # Assuming LABEL_3 corresponds to health
        categorized_tweets["healthTweets"].append(tweet)
    elif label == 'LABEL_4':  # Assuming LABEL_4 corresponds to fashion
        categorized_tweets["fashionTweets"].append(tweet)

# Print categorized tweets to the terminal
print(categorized_tweets)

# Save categorized tweets to a variable
sample_tweets_categorization_data = categorized_tweets

# Save the classification results to separate CSV files
for category, tweets in categorized_tweets.items():
    with open(f'C:/Users/Hp/OneDrive/Desktop/icat/{category}.csv', mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['username', 'tweetText']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for tweet in tweets:
            writer.writerow({'username': tweet['username'], 'tweetText': tweet['tweetText']})