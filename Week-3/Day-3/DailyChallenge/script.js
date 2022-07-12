let form = document.getElementById("form");
let text = document.getElementById("text");
let letters = /^[A-Za-z]+$/
let answer = []

form.addEventListener("submit", function (event){
    event.preventDefault()
    if(text.value.match(letters)){
        sendData()
    }
    else{ 
        alert("Only letters are allowed")
    }    
})