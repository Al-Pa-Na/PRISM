import re

def refine_ocr(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)

    tokens = text.split()

    words = []
    buf = ""

    for t in tokens:
        if len(t) == 1 and t.isalpha():
            buf += t
        else:
            if buf:
                words.append(buf)
                buf = ""
            if len(t) > 1:
                words.append(t)

    if buf:
        words.append(buf)

    return list(dict.fromkeys(words))
