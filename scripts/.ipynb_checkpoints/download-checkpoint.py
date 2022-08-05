print("Running")

import requests

for page_no in range(1,11): #gets 10 pages worth of CAPI data
    url = f'https://content.guardianapis.com/search?page-size=200&page={page_no}&show-fields=trailText,headline,body,byline&api-key=f2652ec5-7f11-4682-bb81-16c0a5e6c850'
    r = requests.get(url, allow_redirects=True)

    open(f'articledata/articles_{page_no}.json', 'wb').write(r.content)
    
print("Done")