require 'httpclient'
require 'json'

headers = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token 81e09a5f8763afe52e37187b7e8f379e566f2dd4'
}

uri = "https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc"

clnt = HTTPClient.new
puts clnt.get_content(uri, headers)
