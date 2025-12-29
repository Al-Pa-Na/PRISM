import os
import httpx
from dotenv import load_dotenv

load_dotenv()

FALLBACK_PRICES = {
    "grocery": {"milk": 54, "banana": 52, "eggs": 68, "bread": 40},
    "electronics": {"headphones": 1999, "mouse": 699, "keyboard": 1499},
    "fashion": {"jeans": 1799, "t shirt": 799, "shoes": 2499}
}

API_URL = "https://real-time-product-search.p.rapidapi.com/search"
HEADERS = {
    "X-RapidAPI-Key": os.getenv("RAPIDAPI_KEY"),
    "X-RapidAPI-Host": "real-time-product-search.p.rapidapi.com"
}

def api_price(item):
    try:
        r = httpx.get(API_URL, headers=HEADERS, params={"q": item}, timeout=10)
        data = r.json()
        products = []
        if isinstance(data.get("data"), dict):
            products = data["data"].get("products", [])
        if products:
            price = products[0].get("price")
            if price:
                return float(price.replace("₹", "").replace(",", ""))
    except:
        pass
    return None

def resolve_price(item, category):
    price = api_price(item)
    if price:
        return price
    return FALLBACK_PRICES.get(category, {}).get(item)
