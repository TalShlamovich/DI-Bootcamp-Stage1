//add an item to the list when clicking the button
function addToList() {
    var li = document.createElement('li');
    var task = document.getElementById('input').value;
    var text = document.createTextNode(task);
    li.appendChild(text);

    //checkmarks
    li.addEventListener('click', function(event){
        console.log(li.innerText);
    })

     //add delete button
    var span = document.createElement('span');
    span.className = "delete";
    var cross = document.createTextNode("\u00D7");
    span.appendChild(cross);
    li.appendChild(span);
    
    //check if field is empty
    if (task.trim().length === 0) {
        return false;
    }
    else {
        document.getElementsByClassName('listTasks')[0].appendChild(li);
    }
    document.getElementById('input').value = "";

   //use delete button
   var remove = document.getElementsByClassName('delete');
   for (i=0; i<remove.length; i++) {
    remove[i].onclick = function() {
        var div = this.parentElement;
        div.style.display = "none";
    }
   }
}
// //check marks (stole this from w3)
// var list = document.querySelector('li');
// list.addEventListener('click', function(event){
//     if (event.target.tagName === 'li') {
//         event.target.classList.add("checked");
//     }
// }, false);
