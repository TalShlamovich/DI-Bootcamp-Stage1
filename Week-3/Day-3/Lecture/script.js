// let id;

// function start() {
//     let index = 0;
//     id = setInterval(function(){
//         index++
//             moveRight(index);
//     },2000)
// }

// var div = document.getElementById('inner');
// var dist = 1; 
// setInterval (function(){
//  var divStart = div.offsetLeft;
//  div.style.left = (divStart + dist) + 'px';

// },1)

function start() {
    let box = document.getElementById('inner');
    let pos = 0;
    let id = setInterval(function(){
        if (pos == 350){
            clearInterval(id);
        }
        pos++
        box.style.left = pos + 'px'
    }, 5)

    // let id1 = setInterval(function(){
    //     if (pos == 350){
    //         clearInterval(id1);
    //     }
    //     pos++
    //     box.style.top = pos + 'px'
    // }, 5)
}