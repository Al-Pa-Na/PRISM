from PIL import Image
from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang="en")

def run_ocr(image_path):
    img = Image.open(image_path).convert("RGB")
    result = ocr.ocr(img)

    text = []
    for line in result:
        for box in line:
            text.append(box[1][0])
    return " ".join(text)
