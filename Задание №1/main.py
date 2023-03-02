import requests

URL = 'https://akabab.github.io/superhero-api/api/all.json'

responce = requests.get(URL)

max_intelligence = 0
data = responce.json()
final_list = []
for i in data:
    if i['name'] == 'Hulk':
        final_list.append(i)
    if i['name'] == 'Thanos':
        final_list.append(i)
    if i['name'] == 'Captain America':
        final_list.append(i)

for i in final_list:
    if max_intelligence < i['powerstats']['intelligence']:
        max_intelligence = i['powerstats']['intelligence']
        most_intelligence_hero = i['name']

print(most_intelligence_hero)
