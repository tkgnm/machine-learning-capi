import json

files = ["articles_1.json", "articles_2.json", "articles_3.json", "articles_4.json", "articles_5.json", "articles_6.json", "articles_7.json", "articles_8.json", "articles_9.json", "articles_10.json"]

results = []

print("Saving...")

for file in files:
        
    # Opening JSON file
    f = open("articledata/" + file)
    
    # returns JSON object as 
    # a dictionary
    # print(data)
    data = json.load(f)
    
    # print((data["response"]["results"][0]))
    
    data = data["response"]["results"]
    
    for item in data:
        results.append(item)
    
    f.close()
    
    
myDict = {"all_articles": results}

with open('data/rawdata.json', 'w') as data:
    json.dump(myDict, data)

print("Finished")