from scraper.price_resolver import resolve_price
from sentiment.sentiment_engine import sentiment_score
from sentiment.aspect_sentiment import aspect_sentiment

def recommend(items):
    out = []

    for it in items:
        price = resolve_price(it["item"], it["category"])
        if price is None:
            continue

        reviews = [
            "Great quality and fresh product",
            "Price is a bit high",
            "Packaging was bad but delivery was fast",
            "Very durable and sturdy build"
        ]

        out.append({
            "item": it["item"],
            "category": it["category"],
            "price": price,
            "sentiment": sentiment_score(reviews),
            "aspects": aspect_sentiment(reviews)
        })
    return out
