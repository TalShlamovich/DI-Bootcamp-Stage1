// 🌟 Exercise 1: Your Favorite Food

//Store your favorite food into a variable.

// Store your favorite meal of the day into a variable (ie. breakfast, lunch or dinner)

// Console.log I eat <favorite food> at every <favorite meal> 

var favFood="a full cup of sugar";
var favMeal="dinner";
var text="I add";
// let diet=text.concat(" ", favFood, " ", "to every"," ", favMeal);
let diet=`${text} ${favFood} to every ${favMeal}`
console.log(diet);

// 🌟 Exercise 2 : Series
// Part I
// Using this array : let myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];

// Create a variable named myWatchedSeriesLength that is equal to the number of series in the myWatchedSeries array.

let myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];
let myWatchedSeriesLength=(myWatchedSeries.length);

// Create a variable named myWatchedSeriesSentence, that is equal to a sentence describing the series you watched
// For example : black mirror, money heist, and the big bang theory

let myWatchedSeriesSentence='black mirror, money heist, and the big bang theory'

// Console.log a sentence using both of the variables created above
// For example : I watched 3 series : black mirror, money heist, and the big bang theory

console.log(`I watched ${myWatchedSeriesLength} series: ${myWatchedSeriesSentence}`);

// Part II
// Change the series “the big bang theory” to “friends”. Hint : You will need to use the index of “the big bang theory” series.

myWatchedSeries[2]='friends'

// Add, at the end of the array, the name of another series you watched.

myWatchedSeries.push('suits');

// Add, at the beginning of the array, the name of your favorite series.

myWatchedSeries.unshift('arrow');

// Delete the series “black mirror”.

myWatchedSeries.splice(1, 1);

// Console.log the third letter of the series “money heist”.

console.log(myWatchedSeries[1][2]);
console.log(myWatchedSeries[1].charAt(2));

// Finally, console.log the myWatchedSeries array, to see all the modifications you’ve made.

console.log(myWatchedSeries);

// 🌟 Exercise 3 : The Temperature Converter
// Instructions
// Store a celsius temperature into a variable.

let celsius=10;

// Convert it to fahrenheit and console.log <temperature>°C is <temperature>°F.

let fahrenheit = celsius * 9/5 + 32;
console.log(fahrenheit);
console.log(celsius *9/5 + 32);

// Hint : Should you create another variable to hold the temperature in fahrenheit? (ie. point 2)
// Hint: To convert a temperature from celsius to fahrenheit : Divide it by 5, then multiply it by 9, then add 32

// 🌟 Exercise 4 : Guess The Answers #1
// Instructions
// For each expression, predict what you think the output will be in a comment (//) without first running the command.
// Of course, explain each prediction.
// Then run the expression in the console. Note the actual output in a comment and compare it with your prediction.

let c;
let a = 34;
let b = 21;

console.log(a+b) //first expression
// Prediction: output will be 55, ie the summ of two numbers
// Actual: 55

a = 2;

console.log(a+b) //second expression
// Prediction: output will be 23. we assign a new value to a.
// Actual: 23

// What is the value of c?
// Prediction: "undefined", because we haven't assigned a value to it
// Actual: undefined

// Analyse the code below, what will be the outcome?
//Prediction: 75. 3 and 4 are numbers, their aum is 7, and 5 is a string, so it's not added arithmetically.
// Actual: 75
console.log(3 + 4 + '5');

// Exercise 5 : Guess The Answers #2
// Instructions
// For each expression, predict what you think the output will be in a comment (//) without first running the command.
// Of course, explain each prediction.
// Then run the expression in the console. Note the actual output in a comment and compare it with your prediction.


console.log(typeof(15))
// Prediction: Number. It's a number and not a string, because there are no quotes or double quotes
// Actual: Number.

console.log(typeof(5.5));
// Prediction: Number. Same as above.
// Actual: Number

console.log(typeof(NaN));
// Prediction: Number. Same as above
// Actual: Number

console.log(typeof("hello"));
// Prediction: String. Because hello is within the double quotes
// Actual: String

console.log(typeof(true));
// Prediction: boolean. True is a boolean
// Actual: True

console.log(typeof(1 != 2));
// Prediction: Boolean. This expression says 1 is not 2
// Actual: Boolean

console.log("hamburger" + "s");
// Prediction: hamburgers. Two strings are concated
// Actual: hamburgers

console.log("hamburgers" - "s");
// Prediction: NaN. Because there is no way to do such a calculation with a string
// Actual: NaN

console.log("1" + "3");
// Prediction: 13. 1 and 3 are treated as strings due to double quotes
// Actual: 13

console.log("1" - "3");
// Prediction: -2. It will try to convert strings into numbers when there is a minus sign.
// Actual: -2

console.log("johnny" + 5);
// Prediction: johnny5. a string and a number are concat together
// Actual:johnny5

console.log("johnny" - 5);
// Prediction: NaN. same as "hamburgers"-"s"
// Actual:NaN

console.log(99 * "hello");
// Prediction: NaN. same as above.
// Actual: NaN

console.log(1 != 1);
// Prediction: False. The expression states that 1 is not equal to 1
// Actual: False

console.log(1 == "1");
// Prediction: True. The expression states that the value of 1 is equal to 1
// Actual:

console.log(1 === "1");
// Prediction: False. The expression states that 1 (number) is equal to 1 (string) in both value and type
// Actual: False

// Exercise 6 : Guess The Answers #3
// Instructions
// For each expression, predict what you think the output will be in a comment (//) without first running the command.
// Of course, explain each prediction.
// Then run the expression in the console. Note the actual output in a comment and compare it with your prediction.

console.log(5 + "34");
// Prediction: 534. A number and a string are concat together.
// Actual: 534

console.log(5 - "4");
// Prediction: 1. It will try to convert strings into numbers when there is a minus sign.
// Actual: 1

console.log(10 % 5);
// Prediction: 0. The remainder of 10/5 is 0
// Actual: 0

console.log(5 % 10);
// Prediction: 5. 5/10=0.5. 5 is a remainder
// Actual: 5

console.log("Java" + "Script");
// Prediction: JavaScript. 2 strings are concat together
// Actual:JavaScript

console.log(" " + " ");
// Prediction: Two blank spaces. concat 2 strings
// Actual: Two blank spaces

console.log(" " + 0);
// Prediction: "blank space"0. same as above
// Actual: "blank space"0

console.log(true + true);
// Prediction: 2. True has a value of 1
// Actual: 2

console.log(true + false);
// Prediction: 1. true is 1 and false is 0
// Actual: 1

console.log(false + true);
// Prediction: 1. Same as above
// Actual: 1

console.log(false - true);
// Prediction: -1. same as above
// Actual: -1

console.log(!true);
// Prediction: false. not true is false
// Actual: false

console.log(3 - 4);
// Prediction: -1. just two numbers here
// Actual: -1

console.log("Bob" - "bill");
// Prediction: NaN. Because there is no way to do such a calculation with a string
// Actual: NaN
