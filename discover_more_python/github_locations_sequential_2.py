import requests, collections, json

response = requests.get('https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc', headers={
  'User-Agent': 'Holberton_School',
  'Authorization': 'token 3f376e3818ab2df8fcacf6cdfc2e68fbd1a63066'
})

repos = [{
    'owner': i['owner']['login'],
    'full_name': i['full_name']
} for i in response.json()['items']]

for repo in repos:
    url = "https://api.github.com/users/" + repo['owner']

    response_2 = requests.get(url, headers={
      'User-Agent': 'Holberton_School',
      'Authorization': 'token 3f376e3818ab2df8fcacf6cdfc2e68fbd1a63066'
    })
    repo['location'] = response_2.json()['location']

new_json = json.dumps([collections.OrderedDict([
    ('full_name', str(item['full_name'])),
    ('location', str(item['location']))
]) for item in repos])

print new_json