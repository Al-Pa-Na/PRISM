from core.pricing import resolve_price
from core.sentiment import sentiment_score, aspect_sentiment

def recommend(items):
    reviews = [
        "Great quality and fresh product",
        "Price is a bit high",
        "Packaging was bad but delivery was fast",
        "Very durable and sturdy build"
    ]

    out = []
    for it in items:
        price = resolve_price(it["item"], it["category"])
        if price is None:
            continue
        out.append({
            "item": it["item"],
            "category": it["category"],
            "price": price,
            "sentiment": sentiment_score(reviews),
            "aspects": aspect_sentiment(reviews)
        })
    return out
