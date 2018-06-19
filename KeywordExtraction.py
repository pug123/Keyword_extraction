# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 17:58:31 2018

@author: Shawlock
"""

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import PyPDF2

nltk.download('punkt')

nltk.download('stopwords')

# creating a pdf file object (set the path in the location of the file)
pdfFileObj = open('JavaBasics-notes.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# printing number of pages in pdf file
print(pdfReader.numPages)

num_pages = pdfReader.numPages
# intializing the random vaariable count
count = 0

text = ""
#The while loop will read each page
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()
#This if statement exists to check if the above library returned #words. It's done because PyPDF2 cannot read scanned files.
if text != "":
   text = text
#The word_tokenize() function will break our text phrases into #individual words
tokens = word_tokenize(text)

#we'll create a new list which contains punctuation we wish to clean
punctuations = ['(',')',';',':','[',']',',']
#We initialize the stopwords variable which is a list of words like #"The", "I", "and", etc. that don't hold much value as keywords
stop_words = stopwords.words('english')

#We create a list comprehension which only returns a list of words #that are NOT IN stop_words and NOT IN punctuations.
keywords = [word for word in tokens if not word in stop_words]
keywords = []
for word in tokens:
    if word not in stop_words:
        keywords.append(word)
print(tokens)
print(keywords)

# closing the pdf file object
pdfFileObj.close()