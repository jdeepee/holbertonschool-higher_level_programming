var https = require('https');
var fs = require('fs');

var options = {
  hostname: 'api.github.com',
  path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
  headers: {
    'User-Agent': 'Holberton_School',
    'Authorization': 'token 61caf9746ee6068ca819094f119c90c96dcd9b49'
  }
}

var req = https.request(options, function(res){

  var waiting = function(finalString){
      var file = '/tmp/14';
      fs.writeFile(file,JSON.stringify(finalString));
      console.log("The file was saved!");
  }

  //Combines response stream into string
  var combine = function streamToString(stream, cb) {
    const chunks = [];
    stream.on('data', (chunk) => {
      chunks.push(chunk);
    });
    stream.on('end', () => {
      cb(chunks.join(''));
    });
  }

  combine(res,function (jsonString) {
    var array = JSON.parse(jsonString);
    var finalArray = [];
    array.items.forEach(function(items){
      var user_options = {
        hostname: 'api.github.com',
        path: '/users/' + items.owner.login + '?q=language:javascript',
        headers: {
          'User-Agent': 'Holberton_School',
          'Authorization': 'token 61caf9746ee6068ca819094f119c90c96dcd9b49'
        }
      }
      var reqUser = https.request(user_options, function(res){
        combine(res,function(jsonStringOwner){
          owner = JSON.parse(jsonStringOwner);
          finalArray.push({
            full_name: items.full_name,
            location: owner.location
          });
          if(finalArray.length == 30){
            waiting(finalArray);
          }
        });
      });
      reqUser.end();
    });
  });
});
req.end();
