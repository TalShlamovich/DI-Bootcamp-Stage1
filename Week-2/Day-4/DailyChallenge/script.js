let phrase = prompt('type a few words separated by commas');
arr = phrase.split(",");
// console.log(phrase);
// console.log(arr);

function frame() {
    for (let i = 0; i < 1; i++) {
        console.log("*******");
        for(j = 0; j < arr.length; j++) {
            // arr = arr[j].split(",");
            console.log("*" + arr[j] + "*");
        }
    }
    console.log("*******");
    console.log(arr);
}
frame()

//idk man I am trying my best here