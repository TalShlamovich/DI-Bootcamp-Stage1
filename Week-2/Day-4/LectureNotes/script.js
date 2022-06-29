// function name() {
//     let a=0;
//     if (a>0){
//         console.log('hello');
//     }
//     else{
//         for (let i = 0; i < 5; i++) {
//             console.log('hello'+i);       
//         }
//     }
// }

// function checkEmail() {
//     let email = 'qwe@qwe.com'
//     if (true) {
//         return true
//     }
//     else {
//         return false
//     }
// }

// let a =checkEmail()
// console.log(a);

function ageCalc(myAge) {
    let mumAge = myAge*2;
    let dadAge = mumAge*1.2;
    console.log(`The age of my mum is ${mumAge} and the age of my dad is ${dadAge}`);
}

let a = ageCalc(50)


function ageCalc2(myAge2) {
    myMumAge = myAge2*2;
    return myMumAge
}

let answer = ageCalc2(20);
console.log(`My mum is ${answer} years old`);