import spacy
nlp = spacy.load('en_core_web_sm')

mystring = '"We \'re moving to L.A.!"'

doc = nlp(mystring)

for token in doc:
    print(token.text)

doc2 = nlp(u"We're here to help! Send snail-mail, email support@ouremail.com")

for token in doc2:
    print(token)

print(len(doc2)) # find out the token length

# 13

doc3 = nlp(u"Apple to build a Hong Kong factory for $6 million")

for token3 in doc3:
    print(token3.text,end='|')


    # Apple|to|build|a|Hong|Kong|factory|for|$|6|million

print("\n")

for tokenentity in doc3.ents:
    print(tokenentity)
    print(tokenentity.label_)  # entity label
    print(str(spacy.explain(tokenentity.label_))) # entity label explaination

#to show in graph
from spacy import displacy

doc4 = nlp(u"Apple to build a Hong Kong factory for $6 million")

displacy.serve(doc4,style="dep")

# result can be seen in browser using http://127.0.0.1:5000/
