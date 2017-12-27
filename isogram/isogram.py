import re

def is_isogram(string):
    regex_pattern = r"(\w).*\1"
    if len(re.findall(regex_pattern,''.join(sorted(string.lower())))) > 0:
        return False
    else:
        return True
