from rapidfuzz import process, fuzz

CANONICAL_ITEMS = [
    "milk", "bread", "banana", "eggs", "rice", "wheat flour",
    "sugar", "salt", "oil", "butter"
]

def normalize_items(items, threshold=70):
    normalized = []
    for item in items:
        match, score, _ = process.extractOne(
            item, CANONICAL_ITEMS, scorer=fuzz.ratio
        )
        if score >= threshold:
            normalized.append(match)
    return list(set(normalized))
