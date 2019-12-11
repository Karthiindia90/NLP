import spacy

nlp = spacy.load("en_core_web_sm")

# print all default stop_words

print(nlp.Defaults.stop_words)

# to findout the default length of the stop_word list

print(len(nlp.Defaults.stop_words))  # Defaults contain 326 words as of tdy 11/12/2019


# to check whether the word is in the stop_words list

print(nlp.vocab["a"].is_stop)

# to add frequest short form words you want

nlp.Defaults.stop_words.add("btw")

nlp.vocab["btw"].is_stop = True

# to check whether btw added in the list
print(nlp.vocab["btw"].is_stop)
print(len(nlp.Defaults.stop_words))


# to remove words from stop_words you want

nlp.Defaults.stop_words.remove("btw")

nlp.vocab["btw"].is_stop = False

# to check whether btw added in the list
print(nlp.vocab["btw"].is_stop)
print(len(nlp.Defaults.stop_words))
