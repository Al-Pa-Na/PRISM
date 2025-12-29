from rapidfuzz import process
from sentence_transformers import SentenceTransformer, util

CATALOG = {
    "grocery": ["milk", "banana", "eggs", "bread", "rice"],
    "electronics": ["headphones", "mouse", "keyboard", "charger"],
    "fashion": ["jeans", "t shirt", "shoes"]
}

model = SentenceTransformer("all-MiniLM-L6-v2")

def refine_text(text):
    text = text.lower()
    words = []
    buf = ""

    for c in text:
        if c.isalpha():
            buf += c
        else:
            if buf:
                words.append(buf)
                buf = ""
    if buf:
        words.append(buf)

    clean = []
    for w in words:
        if 3 <= len(w) <= 15:
            vowel_ratio = sum(c in "aeiou" for c in w) / len(w)
            if vowel_ratio <= 0.7:
                clean.append(w)
    return clean

def semantic_match(tokens, threshold=0.45):
    results = []
    for category, items in CATALOG.items():
        item_emb = model.encode(items, convert_to_tensor=True)
        for t in tokens:
            t_emb = model.encode(t, convert_to_tensor=True)
            scores = util.cos_sim(t_emb, item_emb)[0]
            best = scores.argmax().item()
            if scores[best] >= threshold:
                results.append({
                    "item": items[best],
                    "category": category
                })
    return list({(r["item"], r["category"]): r for r in results}.values())

def process_text(text):
    tokens = refine_text(text)
    return semantic_match(tokens)
