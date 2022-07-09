// 🌟 Exercise 1 : Change The Article
// Instructions
// Using a DOM property, retrieve the h1 and console.log it.

// Using DOM methods, remove the last paragraph in the <article> tag.

// Add a event listener which will change the background color of the h2 to red, when it’s clicked on.

// Add an event listener which will hide the h3 when it’s clicked on (use the display:none property).

// Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.

// BONUS : When you hover on the h1, set the font size to a random pixel size between 0 to 100.

// BONUS : When you hover on the 2nd paragraph, it should fade out (Check out “fade css animation” on Google)

let h1 = document.querySelector('h1');
console.log(h1);

let article = document.querySelector('article');
article.removeChild(article.lastElementChild);

h2 = document.getElementsByTagName('h2')[0];

h2.addEventListener("click", function() {
redOnClick(h2);
});

function removeOnClick(elm){
    elm.remove();
}

function redOnClick(elm) {
    elm.style.backgroundColor = "red";
}

h3 = document.getElementsByTagName('h3')[0];
h3.addEventListener("click", function (){
    hideOnClick(h3);
});

function hideOnClick(elm) {
    elm.style.display = "none";
}

let p = document.getElementsByTagName('p');

function bold() {
    for (i=0; i<p.length; i++)
    p[i].style.fontWeight = "bold";
}

h1.addEventListener("mouseover", function(){
    randomFontOnHover(h1);
});

function randomFontOnHover(elm) {
    elm.style.fontSize = Math.floor(Math.random() * 101) + 'px';
}

// 🌟 Exercise 2 : Work With Forms
// Instructions
// Retrieve the form and console.log it.

// Retrieve the inputs by their id and console.log them.

// Retrieve the inputs by their name attribute and console.log them.

// When the user submits the form (ie. submit event listener)
//      use event.preventDefault(), why ?
//      get the values of the input tags,
//      make sure that they are not empty,
//      create an li per input value,
//      then append them to a the <ul class="usersAnswer"></ul>, below the form.

let submitForm = document.forms[0];
// let submitForm = document.getElementsByTagName('form')[0];
console.log(submitForm);

submitForm.addEventListener('submit', function(e){
    e.preventDefault();

    var firstName = submitForm.querySelector('#fname').value;
    var lastName = submitForm.querySelector('#lname').value;
    
    if (firstName.trim().length === 0 || lastName.trim().length === 0){
        alert("Please fill the form");
        return false;
    }
    else {
        console.log(firstName, lastName);
    }
    

    // create li and insert text
    var li1 = document.createElement('li');
    li1.textContent = firstName;
    var li2 = document.createElement('li');
    li2.textContent = lastName;

    //append to ul
    document.getElementsByClassName('usersAnswer')[0].appendChild(li1);
    document.getElementsByClassName('usersAnswer')[0].appendChild(li2);
})

// 🌟 Exercise 3 : Transform The Sentence
// Instructions
// Declare a global variable named allBoldItems.

// Create a function called getBold_items() that takes no parameter.
// This function should collect all the bold items inside the paragraph and assign them to the allBoldItems variable.

// Create a function called highlight() that changes the color of all the bold text to blue.

// Create a function called return_normal() that changes the color of all the bold text back to black.

// Call the function highlight() onmouseover (ie. when the mouse pointer is moved onto the paragraph),
// and the function return_normal() onmouseout (ie. when the mouse pointer is moved out of the paragraph)
function getBold_items(){
    let inBold = document.querySelectorAll('strong');
    let allBoldItems = [];
    let data;
    for (i=0; i<inBold.length; i++) {
        data = inBold[i].innerText;
        allBoldItems.push(data);
    }
console.log(allBoldItems);
}
getBold_items()

function highlight()