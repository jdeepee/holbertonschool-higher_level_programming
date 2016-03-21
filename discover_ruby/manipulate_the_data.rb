require 'httpclient'
require 'json'

headers = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token 81e09a5f8763afe52e37187b7e8f379e566f2dd4'
}

uri = "https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc"

newcli = HTTPClient.new
json_object = newcli.get_content(uri, headers)
response = JSON.parse(json_object)['items']

names = response.map {|e| e["full_name"]}
puts names.join("\n")