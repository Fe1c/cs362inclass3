import re

def wordcount(string):
    return len(re.findall(r'\w+',string))