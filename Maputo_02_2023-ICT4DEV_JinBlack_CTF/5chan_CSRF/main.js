const cardmsg = document.body;//document.querySelector('.cardmsg');
const data = cardmsg.innerHTML;
const URL = 'https://www.example.com/api/send-message';

fetch(URL, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded'
  },
  body: `data=${encodeURIComponent(data)}`
})
.then(response => {
  // handle the response
  console.log(response);
})
.catch(error => {
  // handle the error
  console.error(error);
  alert('Error: ' + error.message);

});

