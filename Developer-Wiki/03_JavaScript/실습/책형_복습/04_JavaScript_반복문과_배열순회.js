let sum = 0;
for (let i = 1; i <= 3; i++) {
    sum += i;
    console.log(i, sum);
}
for (let row = 1; row <= 3; row++) {
    let line = '';
    for (let column = 1; column <= row; column++) {
        line += '+';
    }
    console.log(line);
}
