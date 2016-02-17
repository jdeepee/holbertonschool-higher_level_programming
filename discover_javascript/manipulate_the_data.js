var https = require('https')

var options = {
  hostname: 'api.github.com',
  path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
  headers: {
    'User-Agent': 'Holberton_School',
    'Authorization': 'token'
  }
};

const chunks = []
var req = https.request(options, function(res){
  console.log(res.statusCode);
  res.on('data', (chunk) => {
    chunks.push(chunk);
  });
  res.on('end', () => {
    var jsonString = chunks.join('');
    var jsonJson = JSON.parse(jsonString);
    console.log(jsonJson);
  });
});

req.end();
req.on('error', function(e) {
  console.error(e);
});
