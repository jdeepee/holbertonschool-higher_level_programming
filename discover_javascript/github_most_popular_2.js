var https = require('https')

var options = {
  hostname: 'api.github.com',
  path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
  headers: {
    'User-Agent': 'Holberton_School',
    'Authorization': 'token 61caf9746ee6068ca819094f119c90c96dcd9b49'
  }
};

const chunks = []
var req = https.request(options, function(res){
  res.on('data', (chunk) => {
    chunks.push(chunk);
  });
  res.on('end', () => {
    var jsonString = chunks.join('');
    console.log(typeof jsonString);
    console.log(jsonString);
  });
});

req.end();
req.on('error', function(e) {
  console.error(e);
});
