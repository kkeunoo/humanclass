let first = 0;
while (first > 0) {
    console.log('while 본문');
    first--;
}
console.log('while 끝', first);
let second = 0;
do {
    console.log('do 본문', second);
    second--;
} while (second > 0);
console.log('do 끝', second);
