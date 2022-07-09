//containers
let orangeSquare = document.getElementById('drop-container');
let pinkSquareContainer = document.getElementsByClassName('draggable-container')[0];
//draggable element
let pinkSquare = document.getElementById('draggable-element');

pinkSquare.addEventListener('dragstart', function(event){
    event.dataTransfer.setData('pink-square', event.target.id);
});

orangeSquare.addEventListener('dragover', function (event) {
    event.preventDefault();
})

orangeSquare.addEventListener('drop', function(event){
    event.preventDefault();
    let id = event.dataTransfer.getData('pink-square');
    let pinkBox = document.getElementById(id);
    event.target.appendChild(pinkBox);
});

pinkSquareContainer.addEventListener('dragover', function(event){
    event.preventDefault();
})