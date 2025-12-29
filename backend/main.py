from core.ocr import run_ocr
from core.nlp import process_text
from core.recommender import recommend

def run(image_path):
    text = run_ocr(image_path)
    items = process_text(text)
    return recommend(items)

if __name__ == "__main__":
    print(run("ocr/sample.jpg"))
