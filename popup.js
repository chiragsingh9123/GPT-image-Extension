const ptag = document.getElementById("info");
const myinp =  document.getElementById("myInput");
ptag.innerHTML =  myinp.value;
url = "";


document.addEventListener('DOMContentLoaded', function () {
    const fileUrl = 'token.txt'; // Replace with the actual URL
    fetch(fileUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.text();
        })
        .then(content => {
            console.log(content);
            url = content;
            
        })
        .catch(error => {
            console.error('Error fetching the file:', error);
        });
});

document.getElementById('myButton').addEventListener('click', function() {
    ptag.innerHTML="";
    fetch( url+'/gen_response?q='+ myinp.value, {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify({ data: "inputData" }),
  })
  .then(response => response.json())
  .then(data => {
      console.log('Response from Python:', data);
      ptag.innerHTML = data['message'];
      console.log(data['message']);
      // Handle the response from the server if needed
  })
  .catch(error => console.error('Error:', error));
    
});

document.getElementById('screenshot').addEventListener('click', function() {
    ptag.innerHTML="";
    fetch(url+'/screen_shot', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify({ data: "inputData" }),
  })
  .then(response => response.json())
  .then(data => {
      console.log('Response from Python:', data);
      ptag.innerHTML = data['message'];
      
      // Handle the response from the server if needed
  })
  .catch(error => console.error('Error:', error));
    
});






