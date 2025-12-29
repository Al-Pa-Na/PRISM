from ocr.ocr_engine import extract_text
from nlp.ocr_refiner import refine_ocr
from nlp.semantic_matcher import semantic_match
from recommender.recommender import recommend

def run(image_path):
    text = extract_text(image_path)
    tokens = refine_ocr(text)
    matches = semantic_match(tokens)

    items = [
        {"item": m["item"], "category": m["category"]}
        for m in matches
    ]

    return recommend(items)

if __name__ == "__main__":
    print(run("ocr/sample.jpg"))
