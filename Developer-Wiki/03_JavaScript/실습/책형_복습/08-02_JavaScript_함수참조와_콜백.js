function sayHi() {
    console.log('안녕');
}
function run(fn) {
    console.log('시작');
    console.log(typeof fn);
    if (typeof fn === 'function') {
        fn();
    }
    console.log('끝');
}
const later = sayHi;
run(later);
