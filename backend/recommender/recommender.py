from scraper.amazon_scraper import fetch_price
from sentiment.sentiment_engine import sentiment_score
from sentiment.aspect_sentiment import aspect_sentiment

def recommend(items):
    out = []
    for item in items:
        price = fetch_price(item)
        if not price:
            continue

        reviews = [
            "Great quality and fresh product",
            "Price is a bit high",
            "Packaging was bad but delivery was fast",
            "Very durable and sturdy build"
        ]

        out.append({
            "item": item,
            "price": price["price"],
            "sentiment": sentiment_score(reviews),
            "aspects": aspect_sentiment(reviews)
        })
    return out
