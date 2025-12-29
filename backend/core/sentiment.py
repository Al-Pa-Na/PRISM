from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

ASPECTS = {
    "quality": ["quality", "fresh", "build"],
    "price": ["price", "cost", "expensive"],
    "durability": ["durable", "sturdy"],
    "delivery": ["delivery", "late", "fast"]
}

def sentiment_score(reviews):
    scores = [sia.polarity_scores(r)["compound"] for r in reviews]
    return round(sum(scores) / len(scores), 3)

def aspect_sentiment(reviews):
    out = {a: [] for a in ASPECTS}
    for r in reviews:
        rl = r.lower()
        for a, keys in ASPECTS.items():
            if any(k in rl for k in keys):
                out[a].append(sia.polarity_scores(r)["compound"])
    return {a: round(sum(v)/len(v), 3) if v else 0.0 for a, v in out.items()}
