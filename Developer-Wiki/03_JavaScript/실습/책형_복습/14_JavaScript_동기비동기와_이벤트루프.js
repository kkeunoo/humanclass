function inner() {
    console.log('안쪽');
}
function outer() {
    console.log('바깥 시작');
    inner();
    setTimeout(function () {
        console.log('예약 첫째');
    }, 0);
    setTimeout(function () {
        console.log('예약 둘째');
    }, 0);
    console.log('바깥 끝');
}
outer();
console.log('현재 코드 끝');
