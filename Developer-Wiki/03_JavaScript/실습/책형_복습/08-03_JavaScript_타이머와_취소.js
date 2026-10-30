const cancelled = setTimeout(function () {
    console.log('취소된 작업');
}, 100);
clearTimeout(cancelled);
let count = 0;
const interval = setInterval(function () {
    count++;
    console.log(count);
    if (count === 3) {
        clearInterval(interval);
        console.log('끝');
    }
}, 30);
console.log('예약 완료');
