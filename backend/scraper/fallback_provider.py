FALLBACK_PRICES = {
    "grocery": {
        "milk": 54,
        "banana": 52,
        "eggs": 68,
        "bread": 40,
        "rice": 62
    },
    "electronics": {
        "headphones": 1999,
        "mouse": 699,
        "keyboard": 1499,
        "charger": 899
    },
    "fashion": {
        "jeans": 1799,
        "t shirt": 799,
        "shoes": 2499
    }
}

def fallback_price(item, category):
    return FALLBACK_PRICES.get(category, {}).get(item)
