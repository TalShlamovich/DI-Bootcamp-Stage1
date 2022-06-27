// 1=='1' -true. the engine converts '1' to number
//'1'==1 - true. the engine converts 1 to string
// 1==='1' - false. taking it as it is
// converts in this order string-number-boolean or boolean-number-string

// let a=6;
// let b=7;
// let c=6;

// if(a===b) {
//     console.log(true);
// }

// else if(c>a){
//     console.log('yes');
// }

// else if(b>c){
//     console.log('no');
// }

// else {
//     console.log(false);
// }

// let age = prompt('How old are you?');

// if(age<18) {
//     alert('Sorry, buddy')
// }

// else if(age==18){
//     alert('congrats on your first year')
// }

// else {
//     alert('here you go, sir/madam')
// }


//teranry operator


// let a=5;
// let b=5;

// (a===b) ? console.log('yes') : console.log('no');
// let num = (a===b) ? 'yes' : 'no';


//switch


// let a = 2 + 2;

// switch (a) {
//   case 3:
//     alert( 'Too small' );
//     break;
//   case 4:
//     alert( 'Exactly!' );
//     break;
//   case 5:
//     alert( 'Too large' );
//     break;
//   default:
//     alert( "I don't know such values" );
// }

// let a = 2 + 2;

// switch (a) {
//   case 4:
//     alert('Right!');
//     break;

//   case 3: // (*) grouped two cases
//   case 5:
//     alert('Wrong!');
//     alert("Why don't you take a math class?");
//     break;

//   default:
//     alert('The result is strange. Really.');
// }


//objects

// let obj = {
//     name: 'John',
//     lastname: 'Miller',
//     age: 24,
//     single: true,
//     address: {
//         street: 'Bezalel',
//         number: 4,
//         city: 'Ramat Gan',
//         zipcode: {
//             number: 879865
//         }
//     },
//     fav: ['banana', 'kiwi', 'ramen'],
//     tv: [
//         {name:'friends'},
//         {name:'breaking bad' ,year:2010},
//         {name: 'stanger things'}
//     ]
// }

// console.log(obj.lastname);
// console.log(obj['lastname']);
// console.log(obj.single);
// console.log(obj.address.city);
// console.log(obj.address.zipcode.number);
// console.log(obj.fav[1]);
// console.log(obj.tv);
// console.log(obj.tv[1].name, obj.tv[1].year);


let obj = {
    username: 'asdf',
    password: 'qwerty1',
}


let database = [obj];

let newsfeed = [
    {username:'one', timeline:'t1'},
    {username:'two', timeline:'t2'},
    {username:'three', timeline:'t3'}
]

console.log(database[0].password);
console.log(newsfeed[2].timeline);
