for (let i=1; i<7; i++) {
    console.log("* ".repeat(i));
}


for (let i=1; i<7; i++) {
    star=""
    for (let j=0; j<i; j++) {
        star +="* ";
    }
    console.log(star);
}