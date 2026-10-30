const block = (a, b) => {
    return a + b;
};
const expression = (a, b) => a + b;
const noReturn = (a, b) => {
    a + b;
};
console.log(block(2, 3));
console.log(expression(2, 3));
console.log(noReturn(2, 3));
