// Instructions
// Create a variable called sentence. The value of the variable should be a string that contains the words “not” and “bad”.
// For example, “The movie is not that bad, I like it”.

let sentence = "This movie is not so bad !";
// console.log(sentence.length);


// Create a variable called wordNot where it’s value is the first appearance (ie. the position) of the substring “not” (from the sentence variable).


let wordNot = sentence.indexOf("not");
// console.log(wordNot);


// Create a variable called wordBad where it’s value is the first appearance (ie. the position) of the substring “bad” (from the sentence variable).

let wordBad = sentence.indexOf("bad");
// console.log(wordBad);

// If the word “bad” comes after the word “not”, you should replace the whole “not…bad” substring with “good”, then console.log the result.

if (wordNot ==-1) {
    console.log(sentence)
}

else if (wordBad > wordNot) {
   console.log(sentence= (`${sentence.substring(0, wordNot)}good${sentence.substring((wordBad+3), sentence.length)}`))
}


// If the word “bad” does not come after “not” or the words are not in the sentence, console.log the original sentence.


