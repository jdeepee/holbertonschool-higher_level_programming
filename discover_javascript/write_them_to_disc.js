var https = require('https')
var fs = require('fs')

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
    fs.appendFile('/tmp/14', jsonString, (err) => {
      if (err) throw err;
      console.log('The data was appended to file!');
    });
  });
});

req.end();
req.on('error', function(e) {
  console.error(e);
});
