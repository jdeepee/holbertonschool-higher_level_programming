import requests

response = requests.get('https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc', headers={
  'User-Agent': 'Holberton_School',
  'Authorization': 'token 3f376e3818ab2df8fcacf6cdfc2e68fbd1a63066'
});

for i in response.json()['items']:
    print i['full_name']