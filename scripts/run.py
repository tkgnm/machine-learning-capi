import numpy as np

### load data

txt_file = open("data/article_ids.txt", "r")
file_content = txt_file.read()

ids = file_content.split("\n")
txt_file.close()

arr = np.load('data/sparseMatrix.npy')

### return id

#example ID
ex = ids[37] #37 is an arbitrary example

#get index positoin of article
input_idx = ids.index(ex)                    
result_idx = np.nanargmax(arr[input_idx]) 

print("SAVE FOR LATER ARTICLE: {}".format(ids[input_idx]))
print("{}".format(ids[input_idx]))

print("\n")

print("RECOMMENDED ARTICLE: {}".format(ids[result_idx]))
print("{}".format(ids[result_idx]))
similarity_score = round(arr[input_idx,result_idx], 3)
print("Similarity score: {}".format(similarity_score))
print("___________")


