from paddleocr import PaddleOCR
from PIL import Image
import numpy as np

ocr = PaddleOCR(use_angle_cls=True, lang="en")

def extract_text(image_path):
    img = Image.open(image_path).convert("RGB")
    img = np.array(img)
    result = ocr.ocr(img)

    lines = []
    for block in result:
        for line in block:
            lines.append(line[1][0])

    return "\n".join(lines)
