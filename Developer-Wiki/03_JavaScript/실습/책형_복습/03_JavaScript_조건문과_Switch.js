let score = 85;
if (score >= 90) {
    console.log('A');
} else if (score >= 80) {
    console.log('B');
} else {
    console.log('C');
}
let hour = 23;
let minute = 51;
minute += 35;
if (minute >= 60) {
    hour++;
    minute -= 60;
}
if (hour >= 24) {
    hour -= 24;
}
console.log(`${hour}시 ${minute}분`);
