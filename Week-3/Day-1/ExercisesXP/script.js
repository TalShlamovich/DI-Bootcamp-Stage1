// 🌟 Exercise 1 : Users
// Instructions
// Add the code above, to your HTML file

// Using Javascript:
// Retrieve the div and console.log it

let div = document.getElementById("container");
console.log(div);

// Change the name “Pete” to “Richard”.

document.querySelector(".list").lastElementChild.innerHTML = "Richard";

// Change each first name of the two <ul>'s to your name.

document.getElementById("container").nextElementSibling.firstElementChild.innerHTML = "Tal";
document.getElementById("container").nextElementSibling.nextElementSibling.firstElementChild.innerHTML = "Tal";

// Delete the <li> that contains the text node “Sarah”.

document.getElementById("container").nextElementSibling.nextElementSibling.children[1].remove();

// Bonus - Using Javascript:
// Add a class called student_list to both of the <ul>'s.

document.getElementById("container").nextElementSibling.classList.add("student_list")
document.getElementById("container").nextElementSibling.nextElementSibling.classList.add("student_list")

// Add the classes university and attendance to the first <ul>.
document.getElementById("container").nextElementSibling.classList.add("university", "attendance")

// 🌟 Exercise 2 : Users And Style
// Instructions

// Add a “light blue” background color and some padding to the <div>.
let a = document.querySelector("body").children[3];
a.style.backgroundColor = "lightBlue";
a.style.padding = "15px";

// Do not display the <li> that contains the text node “John”.

let x = document.querySelector("body").children[4].firstElementChild;
x.style.visibility = "hidden";
// Add a border to the <li> that contains the text node “Pete”.

let y = document.querySelector("body").children[4].lastElementChild;
y.style.border = "2px solid red"
// Change the font size of the whole body.

document.querySelector("body").style.fontSize = "18px"

// Bonus: If the background color of the div is “light blue”, 
// alert “Hello x and y” (x and y are the users in the div).

if (a.style.backgroundColor = "lightBlue") {
    alert(`Hello ${x.innerHTML} and ${y.innerText}`)
}


// 🌟 Exercise 3 : Change The Navbar
// Instructions
// In the <div>, change the value of the id attribute from navBar to socialNetworkNavigation, using the setAttribute method.
document.getElementById("navBar").setAttribute("ID", "socialNetworkNavigation");
// We are going to add a new <li> to the <ul>.
// First, create a new <li> tag (use the createElement method).

let newLi = document.createElement("li");
console.log(newLi);
// Create a new text node with “Logout” as its specified text.

let textNode = document.createTextNode("Logout");
console.log(textNode);
// Append the text node to the newly created list node (<li>).

newLi.appendChild(textNode);
console.log(newLi);
// Finally, append this updated list node to the unordered list (<ul>), using the appendChild method.

document.getElementById("socialNetworkNavigation").firstElementChild.appendChild(newLi);
// Bonus
// Use the firstElementChild and the lastElementChild properties to retrieve the first and last <li> elements from their parent element (<ul>).
// Display the text of each link. (Hint: use the textContent property).

console.log(document.getElementById("socialNetworkNavigation").firstElementChild.firstElementChild.textContent);
console.log(document.getElementById("socialNetworkNavigation").firstElementChild.lastElementChild.textContent)