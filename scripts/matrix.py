#second step after import and merge.

print("Running")

import json
import re
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np   

f = open("data/rawdata.json")

decodedData = json.load(f)

data = decodedData["all_articles"]

headline = []
trailText = []
body = []
ids = []

print("Appending items to array")
for article in data:

    headline.append(article["fields"]["headline"])
    trailText.append(article["fields"]["trailText"])
    body.append(article["fields"]["body"])
    ids.append(article["id"])
    

print("Removing html")
htmlRemover = re.compile('<.*?>') 
newlineRemover = '\n'

# as per recommendation from @freylis, compile once only

def cleanhtml(raw_html):
    cleantext = re.sub(htmlRemover, '', raw_html)
    cleantext = re.sub(newlineRemover, '', cleantext)
    return cleantext

cleanTrailText = []
cleanBody = []

for i in range(len(body)):
    cleanTrailText.append(cleanhtml(trailText[i]))
    cleanBody.append(cleanhtml(body[i]))
    

print("Performing vectorization")

vect = TfidfVectorizer(min_df=1, stop_words="english")
tfidf = vect.fit_transform(cleanBody)                                                                                       
pairwise_similarity = tfidf * tfidf.T 

arr = pairwise_similarity.toarray()     
np.fill_diagonal(arr, np.nan)     
arr = arr.astype('float16') #compress to float 16
print("Saving data")

###before you save, split the data and put it back together in the run.py

np.save("data/sparseMatrix.npy", arr)

textfile = open("data/article_ids.txt", "w")
for element in ids:
    textfile.write(element + "\n")
textfile.close()
    
print("Finished")