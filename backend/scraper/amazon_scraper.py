import random

MOCK_PRICES = {
    "banana": (40, 60),
    "milk": (50, 70),
    "bread": (35, 55),
    "eggs": (80, 120)
}

def fetch_price(item):
    if item not in MOCK_PRICES:
        return None
    low, high = MOCK_PRICES[item]
    return {
        "item": item,
        "price": random.randint(low, high)
    }
