from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

ASPECT_KEYWORDS = {
    "quality": ["quality", "fresh", "build", "material"],
    "price": ["price", "cost", "value", "expensive", "cheap"],
    "durability": ["durable", "lasting", "sturdy", "break"],
    "delivery": ["delivery", "packaging", "late", "fast"]
}

def aspect_sentiment(reviews):
    scores = {a: [] for a in ASPECT_KEYWORDS}

    for r in reviews:
        r_l = r.lower()
        for aspect, keys in ASPECT_KEYWORDS.items():
            if any(k in r_l for k in keys):
                scores[aspect].append(sia.polarity_scores(r)["compound"])

    return {
        a: round(sum(v) / len(v), 3) if v else 0.0
        for a, v in scores.items()
    }
