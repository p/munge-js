import re

def convert(text):
    text = re.sub(r',([\s\n]*\])', r'\1', text)
    return text
