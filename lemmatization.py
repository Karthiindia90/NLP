import spacy

nlp = spacy.load("en_core_web_sm")

doc1 = nlp(u"I am a runner running in a race beacause I love to run")

for token in doc1:
    print(token.text,"\t",token.pos_,"\t",token.lemma,"\t",token.lemma_)

# creating a function to do the same thing again

def show_lemmas(text):
    for token in text:
        print(f'{token.text:{12}},{token.pos_:{6}},{token.lemma:<{22}},{token.lemma_}')


doc2 = nlp(u"I saw you yesterday!")

show_lemmas(doc2)  # using that function
