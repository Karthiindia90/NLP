import PyPDF2
## f-Strings,
#### 1. Print an f-string that displays `NLP stands for Natural Language Processing` using the variables provided."


abbr = "NLP"
fulltext = "Natural Language Processing"
print(f"{abbr} stands for {fulltext}")


# 2. Create a file in the current working directory called `contacts.txt` by running the cell below:"
# 'First_Name Last_Name, Title, Extension, Email'"


#3.Open the file and use .read() to save the contents of the file to a string called `fields`.  Make sure the file is closed at the end.

with open("contact.txt") as f:
    fields = f.read()
    print(fields)


# 4. Use PyPDF2 to open the file `Business_Proposal.pdf`. Extract the text of page 2."


myfile = open("Business_Proposal.pdf",mode="rb")
pdfreader = PyPDF2.PdfFileReader(myfile)
page_two_text= pdfreader.getPage(1).extractText()
myfile.close()

print(page_two_text)

# 5. Open the file `contacts.txt` in append mode. Add the text of page 2 from above to `contacts.txt`.\n",
    # CHALLENGE: See if you can remove the word \"AUTHORS:\""
#
# with open("contact.txt",mode="a") as f:
#     f.write(page_two_text[8:])
#     f.seek(0)

#6. Using the `page_two_text` variable created above, extract any email addresses that were contained in the file `Business_Proposal.pdf`."

import re

pattern = r'[\w]+@[\w]+.\D{3}'
email = re.findall(pattern,page_two_text)
print(email)
