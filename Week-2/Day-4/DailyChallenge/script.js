let words = ["Hello", "World", "in", "a", "frame"];

function longestWordLength(arr) {
  let length = arr[0].length;
  for (let i = 1; i < words.length; i++) {
      if(arr[i].length > length){
        length = arr[i].length;
      }
  }
  return length;
}

function addSpaces(word,length){
  if(word.length == length){
    return "";
  }
  return " ".repeat(length-word.length);
}

function stars () {
  let length = longestWordLength(words);
  console.log("*".repeat(length+4));
  for(x in words){
    console.log('* ' + words[x] + addSpaces(words[x],length) + ' *');
  }
  console.log("*".repeat(length+4));
}
stars();