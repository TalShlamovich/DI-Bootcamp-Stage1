// function Song() {  
//     var bottles;
//     var bottlesLeft;
//     for (i = 99; i >= 1; i--) {

//       if (i == 1) {
//         bottles = "bottle";
//         bottlesLeft = "No bottles of beer on the wall!";
//       }

//        else {
//         bottles = "bottles";
//         bottlesLeft = i - 1 + " bottles of beer on the wall!";
//         } 
        
//       console.log(i+ " " + bottles + " of beer on the wall,"); 
//       console.log(i+ " " + bottles + " of beer,");
//       console.log("Take one down, pass it around,");
//       console.log(bottlesLeft);
//     } 
      
//   }
//   console.log(Song())



function correctSong() {
    var bottlesLeft = 99;
    var bottlesCount = 1;
    var bottlesSentence1;
    var bottlesSentence2;
    var bottlesSentence3;
    var bottles;
    for (i=0; i<bottlesLeft; i++) {
        bottlesLeft -=bottlesCount;
        bottlesCount++;
        console.log(i, bottlesLeft);
        
        if (bottlesLeft==0){
            bottles = "bottle";
            bottlesSentence1 = "No bottle of beer on the wall!";
        }

        else if (bottlesLeft==1) {
            bottles = "bottle";
            bottlesSentence1 = "1 bottle of beer on the wall!"
            bottlesSentence2 = "1 bottle of beer,"
            bottlesSentence3 = `Take ${bottlesCount} down, pass them around,`
        }

        // else if (i>bottlesLeft) {
        //     bottlesSentence1 = `${bottlesLeft} ${bottles} "of beer on the wall!"`;
        //     bottlesSentence2 = `${bottlesLeft} ${bottles} "of beer,"`;
        //     bottlesSentence3 = `Take ${bottlesLeft} down, pass them around,`

        // }

        else {
            bottles = "bottles";
            bottlesSentence1 = `${bottlesLeft} ${bottles} "of beer on the wall!"`;
            bottlesSentence2 = `${bottlesLeft} ${bottles} "of beer,"`;
            bottlesSentence3 = `Take ${bottlesCount} down, pass them around,`
        }
        console.log(bottlesSentence1);
        console.log(bottlesSentence2);
        console.log(bottlesSentence3);
    }
    console.log(bottlesLeft);
    
    bottlesSentence1 = `${bottlesLeft} ${bottles} "of beer on the wall!"`;
    bottlesSentence2 = `${bottlesLeft} ${bottles} "of beer,"`;
    bottlesSentence3 = `Take ${bottlesLeft} down, pass them around,`
    console.log(bottlesSentence1);
    console.log(bottlesSentence2);
    console.log(bottlesSentence3);
}

console.log(correctSong());








// var str = "word in a given string"
// function reverse(str){
//     return str.split("").reverse().join("").split(" ").reverse().join(" ")  
// }

// console.log(reverse(str));

// function reverseWord(str) {
//     let ret = '';
//     for (let i = str.length-1; i >= 0; i--) {
//         ret+=str[i];
//     }
//     return ret;
// }

// function reverseAll(str) {
//     let arr = str.split(' ');
//     let ret = '';
//     for (i=0; i<arr.length; i++) {
//         ret.push(reverseWord(arr[i]))
//     }
//     return ret.join(' ');   
// }