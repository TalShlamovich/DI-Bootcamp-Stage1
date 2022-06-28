console.log(0);
console.log(1);
console.log(2);
console.log(3);
console.log(4);

for(let i=0; i<5; i++) {  //start, end, increment
    console.log(i)
}

let arr=['a', 'b', 'c', 'd', 'e']

for(let i=0; i<arr.length; i++) {
    console.log(i, arr[i]);
}

for(x in arr) {
    console.log(x, arr[x]);
}

for (x of arr){
    console.log(x);
}

arr.forEach((item, i) => {
    console.log(i);
})

//arr.map
//arr.filter
//arr.sort
//arr.find
//arr.findIndex

let obj = {
    name: 'John',
    last: 'Miller',
    age: 18
}

for (x in obj) {
    console.log(x, obj[x]);
}




//exercise
// Write a JavaScript for loop that will iterate from 0 to 15.
// For each iteration, it will check if the current number is odd or even, 
// and display a message to the screen.


for(let i=0; i<16; i++) {
    if(i %2 ==0) {
        console.log(`${i} is even`)
    }
    else {
        console.log(`${i} is odd`);
    }
}   
//end of exercise

// let i = 0
// while(i < 7) {
//     console.log(i);
//     i=i+2;
// }

// let i=0;
// do{
//     console.log(i);
//     i=i+2;
// }
// while(i<0)


let object = {
    name: 'John',
    last: 'Miller',
    age: 18
}

let array = Object.keys(object);
console.log(array);

let array1 = Object.values(object);
console.log(array1);

let array2 = Object.entries(object);
console.log(array2);

//Exercise 2
// 1. Write a JavaScript for loop that will go through the variable names.
//   if the item is not a string, pass.
//   if the item is a string, check if its first letter is in uppercase. If not, change it to uppercase and then display the name.
// 2. Write a JavaScript for loop that will go through the variable names
//   if the item is not a string, go out of the loop.
//   if the item is a string, display it.

let names= ["john", "sarah", 23, "Rudolf",34]
for (i=0; i < names.length; i++) {
    if (typeof names[i]=="number") {
        continue;   
    }

    // else if ((names[i].charAt(0).toUpperCase()==names[i].charAt(0))) {
    //     continue;
    // }

    else if(names[i].charAt(0).toLowerCase()==names[i].charAt(0)) {
        names[i]=names[i].charAt(0).toUpperCase() + names[i].substring(1, names[i].length);
    }
    console.log(names[i]);
}

