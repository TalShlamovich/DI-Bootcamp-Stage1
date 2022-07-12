// 🌟 Exercise 1: Timer
// Instructions
// Part I
// In your Javascript file, using setTimeout, call a function after 2 seconds.
// The function will alert “Hello World”.


// Part II
// In your Javascript file, using setTimeout, call a function after 2 seconds.
// The function will add a new paragraph <p>Hello World</p> to the <div id="container">.


// Part III
// In your Javascript file, using setInterval, call a function every 2 seconds.
// The function will add a new paragraph <p>Hello World</p> to the <div id="container">.
// The interval will be cleared (ie. clearInterval), when the user will click on the button.
// Instead of clicking on the button, the interval will be cleared (ie. clearInterval) as soon as there will be 5 paragraphs inside the <div id="container">.

// setTimeout(HelloWorld, 2000);

// function HelloWorld() {
//     alert("Hello World");
// }

// let container = document.getElementById("container");

// setTimeout(addParagraph, 2000);

// function addParagraph() {
//     let newParagraph = document.createElement("p");
//     let text = document.createTextNode("Hello World");
//     newParagraph.appendChild(text);
//     container.appendChild(newParagraph);
// }

// let timer = setInterval(addParagraphInterval, 2000);

// let counter = 0;

// function addParagraphInterval() {
//     let helloWorld = document.createElement("p");
//     let text = document.createTextNode("Hello World");
//     helloWorld.appendChild(text);
//     container.appendChild(helloWorld);
//     counter++;

//     if (counter == 4) {
//         clearInterval(timer);
//     }
// }

// let button = document.getElementById("clear");

// button.addEventListener("click", clear);

// function clear() {
//     clearInterval(timer);
// }


// 🌟 Exercise 2 : Move The Box
// Instructions
// Copy the code above, to a structured HTML file.
// In your Javascript file, use setInterval to move the <div id="animate"> to the right side of the <div id="container">, when the button is clicked on.
// The <div id="animate"> should move 1px to the right every milisecond, until it reaches the end of the <div id="container">.
// Hint : use clearInterval as soon as the box reaches the right end side of the container
// Hint : check out the demonstration in the Course Noted named JS Functions

// function myMove() {
//     let box = document.getElementById('animate');
//     let pos = 0;
//     let id = setInterval(function(){
//         if (pos == 350){
//             clearInterval(id);
//         }
//         pos++
//         box.style.left = pos + 'px'
//     }, 5)
// }


// 🌟 Exercise 3: Drag & Drop
// Instructions
// Copy the code above, to a structured HTML file.
// In your Javascript file add the functionality which will allow you to drag the box and drop it into the target.
// Check out the Course Notes named DOM animations.

// let box = document.getElementById("box")

// box.addEventListener("dragend",function(event){
// let x = event.clientX
//     let y = event.clientY
//     box.style.left = x + "px"
//     box.style.top= y + "px"
// })