def is_polindrom(text):
    if len(text) > 100:
        return "Text is longer than 100 characters"
    text = str(text)
    text = text.lower()
    #text = text.replace(" ","")
    rev_text = text[::-1]
    if text == rev_text:
        return True
    else:
        return False