// 🌟 Exercise 1 : Information
// Instructions
// Part I : function with no parameters
// Create a function called infoAboutMe() that takes no parameter.
// The function should console.log a sentence about you (ie. your name, age, hobbies ect…).
// Call the function.

function infoAboutMe() {
    console.log('My name is Tal and I am 26 yo');
}

let a = infoAboutMe()

// Part II : function with three parameters
// Create a function called infoAboutPerson(personName, personAge, personFavoriteColor) that takes 3 parameters.
// The function should console.log a sentence about the person
// (ie. “You name is …, you are .. years old, your favorite color is …”)
// Call the function twice with the following arguments:
// infoAboutPerson("David", 45, "blue")
// infoAboutPerson("Josh", 12, "yellow")

function infoAboutPerson(personName, personAge, personFavouriteColour) {
    console.log(`${personName}, you are ${personAge} years old and your favourite color is ${personFavouriteColour}`);
}

let David = infoAboutPerson("David", 45, "blue");
let Josh = infoAboutPerson("Josh", 12, "yellow");

// 🌟 Exercise 2 : Tips
// Instructions
// John created a simple tip calculator to help calculate how much to tip when he and his family go to restaurants.

// Create a function named calculateTip() that takes no parameter.

// Inside the function, ask John for the amount of the bill.
// Here are the rules
// If the bill is less than $50, tip 20%.
// If the bill is between $50 and $200, tip 15%.
// If the bill is more than $200, tip 10%.
// Console.log the tip amount and the final bill (bill + tip).
// Call the calculateTip() function.

// function calculateTip() {
//     let bill = prompt ('Enter the bill amount');
//     bill = Number(bill);
//     if (bill < 50) {
//         tip = bill/5
//     }
//     else if (bill>=50 && bill<= 200) {
//         tip = bill*15/100
//     }
//     else {
//         tip = bill/10
//     }
//     console.log(tip, bill + tip);
// }

// let ex2= calculateTip();


// 🌟 Exercise 3 : Find The Numbers Divisible By 23
// Instructions
// Create a function call isDivisible() that takes no parameter.

// In the function, loop through numbers 0 to 500.

// Console.log all the numbers divisible by 23.

// At the end, console.log the sum of all numbers that are divisible by 23.
// Bonus: Add a parameter divisor to the function.

// function isDivisible(divisor) {
//     let summ = 0
//     for (i=0; i<501; i++) {
//         if (i % divisor == 0) {
//             console.log(i);
//             summ += i
//         }
//     }   
//     console.log(summ); 
// }

// let ex3 = isDivisible(3);


// 🌟 Exercise 4 : Shopping List
// Instructions

let stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

let prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

// Create an array called shoppingList with the following items: “banana”, “orange”, and “apple”.
// It means that you have 1 banana, 1 orange and 1 apple in your cart.

let shoppingList = ["banana", "orange", "apple"];

// Create a function called myBill() that takes no parameters.

// The function should return the total price of your shoppingList.
// In order to do this you must follow these rules:
// The item must be in stock. (Hint : check out if .. in)
// If the item is in stock find out the price in the prices object.

function myBill() {
    bill = 0
    for (i of shoppingList) {
        if (i in stock && stock[i] !==0) {
            bill +=prices[i];
            stock[i] -= 1;
        } 
        
    } 
    console.log(bill);
}

let ex4 = myBill()
console.log(stock.banana);
// Call the myBill() function.
// Bonus: If the item is in stock, decrease the item’s stock by 1


// Exercise 5 : What’s In My Wallet ?
// Instructions
// Note: Read the illustration (point 4), while reading the instructions

// Create a function named changeEnough(itemPrice, amountOfChange) that receives two arguments :
// an item price
// and an array representing the amount of change in your pocket.

// In the function, determine whether or not you can afford the item.
// If the sum of the change is bigger or equal than the item’s price (ie. it means that you can afford the item), the function should return true
// If the sum of the change is smaller than the item’s price (ie. it means that you cannot afford the item) the function should return false

// Change will always be represented in the following order: quarters, dimes, nickels, pennies.

// 🌟 Exercise 6 : Vacations Costs
// Instructions
// Let’s create functions that calculate your vacation’s costs:

// Define a function called hotelCost().
// It should ask the user for the number of nights they would like to stay in the hotel.
// If the user doesn’t answer or if the answer is not a number, ask again.
// The hotel costs $140 per night. The function should return the total price of the hotel.

function hotelCost(numNights) {
    let stayCost = 0;
    // let numNights=0;
    // do {
    //     numNights = prompt('How many nights? ($140 per night)');
    //     numNights=Number(numNights)
    // } while (isNaN(numNights) || numNights==0);   
    stayCost = numNights*140
    console.log(`Your total is $${stayCost}`);
    return stayCost
}

// hotelCost()

// Define a function called planeRideCost().
// It should ask the user for their destination.
// If the user doesn’t answer or if the answer is not a string, ask again.
// The function should return a different price depending on the location.
// “London”: 183$
// “Paris” : 220$
// All other destination : 300$

function planeRideCost(destination){
    // let destination = "";
    let ridePrice = 0;
    // do {
    //     destination = prompt("where do you want to fly?").toLowerCase()

    // } while (!isNaN(destination) || destination =="");

    if(destination === "london"){
        ridePrice = 183;
    } else if( destination === "paris"){
        ridePrice = 220;
    } else{
         ridePrice = 300;
    }
    console.log(ridePrice);
    return ridePrice
}
// planeRideCost();

// Define a function called rentalCarCost().
// It should ask the user for the number of days they would like to rent the car.
// If the user doesn’t answer or if the answer is not a number, ask again.
// Calculate the cost to rent the car. The car costs $40 everyday.
// If the user rents a car for more than 10 days, they get a 5% discount.
// The function should return the total price of the car rental.

function rentalCarCost(numDays) {
    // let numDays = 0;
    let carPrice = 0;
    // do {
    //     numDays = prompt('How many days?');
    //     numDays=Number(numDays)
    // } while (isNaN(numDays) || numDays==0); 
    if (numDays<11) {
        carPrice = numDays*40;
    }
    else {
        carPrice = numDays*4*95/10
    }
    console.log(carPrice);
    return carPrice
}
// rentalCarCost()


// Define a function called totalVacationCost() that returns the total cost of the user’s vacation by calling the 3 functions that you created above.
// Example : The car cost: $x, the hotel cost: $y, the plane tickets cost: $z.
// Hint: You have to call the functions hotelCost(), planeRideCost() and rentalCarCost() inside the function totalVacationCost().

// Call the function totalVacationCost()

// Bonus: Instead of using a prompt inside the 3 first functions, only use a prompt inside the totalVacationCost() function.
// You need to change the 3 first functions, accordingly.

function totalVacationCost() {
//    
    do {
        numNights = prompt('How many nights? ($140 per night)');
        numNights=Number(numNights)
    } while (isNaN(numNights) || numNights==0);

    let a = hotelCost(numNights)
//
//
    do {
        destination = prompt("where do you want to fly?").toLowerCase()

    } while (!isNaN(destination) || destination =="");
    
    let c = planeRideCost(destination)
//
//
    do {
        numDays = prompt('How many days?');
        numDays=Number(numDays)
    } while (isNaN(numDays) || numDays==0);

    let b = rentalCarCost(numDays)

    return (a + b + c)
}
// totalVacationCost()
console.log(totalVacationCost());

