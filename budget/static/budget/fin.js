document.addEventListener('DOMContentLoaded', function() {

    document.querySelector('#transfer-form').addEventListener('submit', transfering);
    
});

//API call to transfer money
function transfering() {
    
    fetch('/transferfunc', {
        method: 'POST',
        body: JSON.stringify({
        recipient: document.querySelector('#transfer-recipient').value,
        amount: document.querySelector('#trasnfer-amount').value,
        message: document.querySelector('#transfer-message').value,
        
        })
    })
    
    
   
}

