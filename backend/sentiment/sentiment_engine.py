from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

def sentiment_score(reviews):
    scores = [sia.polarity_scores(r)["compound"] for r in reviews]
    return round(sum(scores) / len(scores), 3) if scores else 0
