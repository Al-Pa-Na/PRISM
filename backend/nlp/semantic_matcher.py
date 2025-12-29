from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

CATALOG = {
    "grocery": ["milk", "banana", "eggs", "bread", "rice", "oil"],
    "electronics": ["headphones", "charger", "power bank", "mouse"],
    "fashion": ["t shirt", "jeans", "dress", "shoes"]
}

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
                    "token": t,
                    "item": items[best],
                    "category": category,
                    "score": float(scores[best])
                })
    return results
