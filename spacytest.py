import spacy
nlp = spacy.load("en_core_web_sm") # creating model
doc = nlp(u"Tesla is looking at buying U.S. startup for $6 million") # unicode string, each word will be changed to token

for token in doc:
    print(token,token.pos_,token.dep_)

print(nlp.pipeline)

print(nlp.pipe_names)

#creating another doc object

doc2 = nlp(u"Tesla isn't    looking into startups anymore.")
for token in doc2:
    print(token,token.pos_,token.dep_)

print(doc2[0])
print(doc2[0].pos_)
print(doc2[0].dep_) #dependency

doc3 =  nlp(u"Although commmonly attributed to John Lennon from his song 'Beautiful Boy', \\\n",
    "the phrase \"Life is what happens to us while we are making other plans\" was written by \\\n")


life_quote= doc3[:10]

type(life_quote) #spacy will find this as span not a doc

type(doc3) #spacy will find this as a doc

print(life_quote)
