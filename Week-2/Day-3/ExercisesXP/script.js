// 🌟 Exercise 1 : List Of People
// Instructions

let people = ["Greg", "Mary", "Devon", "James"];


// Part I - Review About Arrays
// Write code to remove “Greg” from the people array.

people = people.slice(1);


// Write code to replace “James” to “Jason”.

people[2]="Jason";


// Write code to add your name to the end of the people array.

people.push("Tal");

// Write code that console.logs Mary’s index. take a look at the indexOf method on Google.

console.log(people.indexOf("Mary"));

// Write code to make a copy of the people array using the slice method.
// The copy should NOT include “Mary” or your name.
// Hint: remember that now the people array should look like this let people = ["Mary", "Devon", "Jason", "Yourname"];
// Hint: Check out the documentation for the slice method

people1=people.slice(1, 3);
console.log(people1);

// Write code that gives the index of “Foo”. Why does it return -1 ?

console.log(people.indexOf("Foo")); //-1 means "no match found".
//The reason it returns -1 instead of "false" is that an index at the beginning of the string would be 0, which is equivalent to false

// Create a variable called last which value is the last element of the array.
// Hint: What is the relationship between the index of the last element in the array and the length of the array?

let last = people.slice(people.length-1)

console.log(people);

// Part II - Loops
// Using a loop, iterate through the people array and console.log each person.

for ( let i=0; i<people.length; i++) {
    console.log(people[i]);
}

// Using a loop, iterate through the people array and exit the loop after you console.log “Jason” .
// Hint: take a look at the break statement in the lesson.

for (let i=0; i<people.length; i++) {
    console.log(people[i]);
    if (people[i]=="Jason") {
        break;
    }
}

// 🌟 Exercise 2 : Your Favorite Colors
// Instructions
// Create an array called colors where the value is a list of your five favorite colors.

let colors = ["red", "orange", "yellow", "green", "blue"]
// Loop through the array and as you loop console.log a string like so: “My #1 choice is blue”, “My #2 choice is red” ect… .

for (let i=0; i<colors.length; i++) {
    console.log(`My #${i} choice is ${colors[i]}`);
}

// Bonus: Change it to console.log “My 1st choice”, “My 2nd choice”, “My 3rd choice”, picking the correct suffix for each number.
// Hint : create an array of suffixes to do the Bonus

let suff = ["st", "nd", "rd", "th"];
for (let i=0; i<colors.length; i++) {
    if (i<3 ){
        console.log(`My ${i+1}${suff[i]} choice is ${colors[i]}`);
    }
    else {
        console.log(`My ${i+1}${suff[3]} choice is ${colors[i]}`);
    }
}

// 🌟 Exercise 3 : Repeat The Question
// Instructions
// Prompt the user for a number.

let num = prompt("Number please")


// Hint : Check the data type you receive from the prompt (ie. Use the typeof method)

num=Number(num);

// While the number is smaller than 10 continue asking the user for a new number.
// Tip : Which while loop is more relevant for this situation?

while (num<10) {
    num++;
    num = prompt("Number please")
}


// 🌟 Exercise 4 : Building Management
// Instructions:

let building = {
    numberOfFloors : 4,
    numberOfAptByFloor : {
        firstFloor : 3,
        secondFloor : 4,
        thirdFloor : 9,
        fourthFloor : 2,
    },
    nameOfTenants : ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan :  [4, 1000],
        david : [1, 500],
    },
}


// Review About Objects

// Console.log the number of floors in the building.

console.log(building.numberOfFloors);

// Console.log how many apartments are on the floors 1 and 3.

console.log(building.numberOfAptByFloor.firstFloor, building.numberOfAptByFloor.thirdFloor);

// Console.log the name of the second tenant and the number of rooms he has in his apartment.

console.log(building.nameOfTenants[1], building.numberOfRoomsAndRent.dan[0]);

// Check if the sum of Sarah’s and David’s rent is bigger than Dan’s rent. If it is, than increase Dan’s rent to 1200.

let sarahRent = building.numberOfRoomsAndRent.sarah[1];
let danRent = building.numberOfRoomsAndRent.dan[1];
let davidRent = building.numberOfRoomsAndRent.david[1];

if (sarahRent+davidRent > danRent) {
    danRent=1200
}
console.log(danRent);

// 🌟 Exercise 5 : Family
// Instructions
// Create an object called family with a few key value pairs.

let family = {
    daughter: 'Samantha',
    father : 'John',
    mother : 'Maria',
    son: 'Richard',
}

// Using a for in loop, console.log the keys of the object.
for (x in family) {
    console.log(x);
}
// Using a for in loop, console.log the values of the object.

for (x in family) {
    console.log(family[x]);
}