import requests

response = requests.get('https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc', headers={
  'User-Agent': 'Holberton_School',
  'Authorization': 'token 3f376e3818ab2df8fcacf6cdfc2e68fbd1a63066'
})

with open('/tmp/14', 'w') as f:
    f.write(str(response.json()))

print "The file was saved!"