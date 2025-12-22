from scraper.amazon_scraper import fetch_price
from sentiment.sentiment_engine import sentiment_score

def recommend(items):
    recommendations = []

    for item in items:
        price_data = fetch_price(item)
        if not price_data:
            continue

        reviews = [
            "Good quality product",
            "Value for money",
            "Packaging could be better"
        ]

        recommendations.append({
            "item": item,
            "price": price_data["price"],
            "sentiment": sentiment_score(reviews)
        })

    return recommendations
