require 'httpclient'
require 'json'

headers = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token 81e09a5f8763afe52e37187b7e8f379e566f2dd4'
}

filename = '/tmp/14'
uri = "https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc"
target = open(filename,'w')
target.truncate(0)
newcli = HTTPClient.new

response = newcli.get_content(uri, headers)
target.write(response)
puts "The file was saved!"
target.close