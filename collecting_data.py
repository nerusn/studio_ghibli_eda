import requests
import json

#No api key required for this api
base_endpoint = 'https://ghibliapi.herokuapp.com/films'
response = requests.get(base_endpoint)
packages_json = response.json()

#Testing endpoint
print(response.status_code)

#Length of dataset
print("length of dataset is ",len(packages_json))

#Store all 20 dictionaries in empty list

results = []

for package in packages_json:
    package_id = package['id']
    package_title = package['title']
    package_director = package['director']
    package_score = package['rt_score']
    
    package_url = f'https://ghibliapi.herokuapp.com/films/{package_id}'
    
    response = requests.get(package_url)
    package_json = response.json()
    
    data = {
            'title' : package_title,
            'director' : package_director,
            'score' : package_score 
            }
    
    results.append(data) 
    #time.sleep not required due to only 20 entries in data

with open('ghibli_data.json', 'w') as f:
    json.dump(results, f, indent = 2)