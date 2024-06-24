import nltk
nltk.download('vader_lexicon')


from textblob import TextBlob

def analyze_sentiment_textblob(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    return sentiment.polarity, sentiment.subjectivity

text = "I love using Tattiana AI for all my projects!"
polarity, subjectivity = analyze_sentiment_textblob(text)
print(f'Polarity: {polarity}, Subjectivity: {subjectivity}')



from nltk.sentiment.vader import SentimentIntensityAnalyzer

def analyze_sentiment_vader(text):
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)
    return sentiment

text = "I love using Tattiana AI for all my projects!"
sentiment = analyze_sentiment_vader(text)
print(f'Sentiment: {sentiment}')




from transformers import pipeline

def analyze_sentiment_transformers(text):
    sentiment_pipeline = pipeline("sentiment-analysis")
    sentiments = sentiment_pipeline(text)
    return sentiments

text = "I love using Tattiana AI for all my projects!"
sentiments = analyze_sentiment_transformers([text])
print(f'Sentiments: {sentiments}')




import requests
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from transformers import pipeline

def analyze_text(text):
    # TextBlob
    blob = TextBlob(text)
    polarity, subjectivity = blob.sentiment.polarity, blob.sentiment.subjectivity
    
    # VADER
    sia = SentimentIntensityAnalyzer()
    vader_sentiment = sia.polarity_scores(text)
    
    # Transformers
    sentiment_pipeline = pipeline("sentiment-analysis")
    transformers_sentiment = sentiment_pipeline(text)
    
    return {
        "textblob": {"polarity": polarity, "subjectivity": subjectivity},
        "vader": vader_sentiment,
        "transformers": transformers_sentiment
    }

# Example texts
social_media_text = "Just tried the new feature in Tattiana AI, and it's awesome!"
customer_review_text = "The customer service was terrible, I'm never buying from here again."
news_article_text = "Tattiana AI has been nominated as the best AI tool of the year."

for text in [social_media_text, customer_review_text, news_article_text]:
    sentiment_analysis = analyze_text(text)
    print(f'Text: {text}\nSentiment Analysis: {sentiment_analysis}\n')
