import nltk
from nltk.stem.snowball import SnowballStemmer

s_stem = SnowballStemmer(language="english")

words = ["run","running","ran","quick","quickly","fair","fairly","early"]

for word in words:
    print(word + "------->" + s_stem.stem(word))
