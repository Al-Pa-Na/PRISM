from scraper.price_provider import fetch_price
from scraper.fallback_provider import fallback_price

def resolve_price(item, category):
    api_price = fetch_price(item)
    if api_price:
        return api_price["price"]
    return fallback_price(item, category)
