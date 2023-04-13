import praw
from nltk.sentiment.vader import SentimentIntensityAnalyzer


# create an app before starting the analysis
# create reddit instance using PRAW and authenticate with client secret
reddit = praw.Reddit(client_id='app id',
                     client_secret=' app client secret',
                     username='your-reddit-username',
                     password='reddit-password',
                     user_agent='any user agent')


# extract posts from a specified subreddit.
def get_posts(subreddit_name):
    subreddit = reddit.subreddit(subreddit_name)
    posts = []
    for post in subreddit.top(limit=100):
        posts.append(post.title + " " + post.selftext)
    return posts


# function to analyze the sentiment of each post using the VaderSentimentAnalyzer from nltk.
def analyze_sentiment(post):
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(post)['compound']
    return sentiment_score


# function to determine the sentiment
def get_sentiment(sentiment_score):
    if sentiment_score >= 0:
        return "positive"
    else:
        return "negative"


# Put it all in main function and run the bot.
def main():
    subreddit_name = input("Enter the subreddit name: ")
    posts = get_posts(subreddit_name)
    for post in posts:
        sentiment_score = analyze_sentiment(post)
        sentiment = get_sentiment(sentiment_score)
        print("Post: ", post)
        print("Sentiment: ", sentiment)
        print()


if __name__ == '__main__':
    main()
