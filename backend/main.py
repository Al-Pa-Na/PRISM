from ocr.ocr_engine import extract_text
from nlp.item_extractor import extract_items
from nlp.normalizer import normalize_items
from recommender.recommender import recommend

def run(image_path):
    text = extract_text(image_path)
    raw_items = extract_items(text)
    items = normalize_items(raw_items)
    return recommend(items)

if __name__ == "__main__":
    print(run("ocr/sample.jpg"))

