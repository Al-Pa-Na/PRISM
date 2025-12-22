import re

def extract_items(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", " ", text)
    words = text.split()

    items = []
    current = []

    for w in words:
        if len(w) <= 1:
            continue
        current.append(w)
        if len(current) == 2:
            items.append(" ".join(current))
            current = []

    if current:
        items.append(current[0])

    return list(dict.fromkeys(items))
