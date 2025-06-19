import csv

def read_fetched_tweets(file_path):
    tweets = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Skip the header row
        for row in csv_reader:
            tweets.append(row)
    return tweets

# Example usage
file_path = 'fetched_tweets.csv'
tweets = read_fetched_tweets(file_path)
print(tweets)


