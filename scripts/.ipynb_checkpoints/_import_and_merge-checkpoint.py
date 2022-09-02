import json

files = ["articles_1.json", "articles_2.json", "articles_3.json", "articles_4.json", "articles_5.json", "articles_6.json", "articles_7.json", "articles_8.json", "articles_9.json", "articles_10.json"]

results = []

for file in files:
    
    print(f'Opening {file}')
        
    # Opening JSON file
    f = open("articledata/" + file)
    
    # returns JSON object as 
    # a dictionary
    # print(data)
    data = json.load(f)
    
    # print((data["response"]["results"][0]))
    
    data = data["response"]["results"]
    
    print("Appending items to array")
    for item in data:
        results.append(item)
    
    f.close()
    
print ("Creating dictionary")
myDict = {"all_articles": results}

print("Writing to disk")
with open('data/rawdata.json', 'w') as data:
    json.dump(myDict, data)

print("Finished")