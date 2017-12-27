import re
import string

def is_pangram(sentence):
    regex_pattern = r"[a-z]"
    alphabet_list = set(re.findall(regex_pattern, sentence.lower()))
    return alphabet_list.issuperset(string.ascii_lowercase)
