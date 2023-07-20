import re


def match_all_uppercase_word(text):
    pattern = r"\b[A-Z]+\b"  # "\s[A-Z]+\s"  # or
    return re.findall(pattern, text)
