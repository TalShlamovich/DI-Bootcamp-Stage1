var addressNumber="1";
var addressStreet="Dizengoff";
var country="Israel";
var text="I live in"
let globalAddress= text.concat(" ", country," ", addressStreet, " ", addressNumber);

console.log(globalAddress);

var birthYear=1995;
var year=2050;
var age=(year-birthYear);
var filler1="In";
var filler2="I will be"
let sentense=filler1.concat(" ", year, " ", filler2, " ", age);
console.log(sentense);
