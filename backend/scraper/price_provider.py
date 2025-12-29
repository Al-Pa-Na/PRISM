import os
import httpx
from dotenv import load_dotenv

load_dotenv()

SEARCH_URL = "https://real-time-product-search.p.rapidapi.com/search"

HEADERS = {
    "X-RapidAPI-Key": os.getenv("RAPIDAPI_KEY"),
    "X-RapidAPI-Host": "real-time-product-search.p.rapidapi.com"
}

def fetch_price(item):
    r = httpx.get(
        SEARCH_URL,
        headers=HEADERS,
        params={"q": item, "country": "in", "language": "en"},
        timeout=15
    )

    data = r.json()

    products = []
    if isinstance(data.get("data"), dict):
        products = data["data"].get("products") or data["data"].get("items") or []
    elif isinstance(data.get("data"), list):
        products = data["data"]

    if not products:
        return None

    p = products[0]
    price = p.get("price") or p.get("price_amount")
    if not price:
        return None

    try:
        price = float(str(price).replace("₹", "").replace(",", "").strip())
    except:
        return None

    return {"item": item, "price": price}
