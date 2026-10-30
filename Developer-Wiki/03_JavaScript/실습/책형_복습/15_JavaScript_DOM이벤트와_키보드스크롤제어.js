function writeLog(message) {
    const p = document.createElement('p');
    p.textContent = message;
    document.getElementById('view').prepend(p);
    console.log(message);
}
const first = document.getElementById('first');
first.onclick = function () { console.log('교체 전'); };
first.onclick = function () { console.log('교체 후'); };
const second = document.getElementById('second');
second.addEventListener('click', function () { console.log('첫째'); });
second.addEventListener('click', function () { console.log('둘째'); });
function removedHandler() { console.log('제거한 함수'); }
const removed = document.getElementById('removed');
removed.addEventListener('click', removedHandler);
removed.removeEventListener('click', removedHandler);
function checkInput() {
    const user = document.getElementById('user');
    const password = document.getElementById('password');
    const warning = document.getElementById('warning');
    if (user.value.trim() === '') {
        warning.textContent = '아이디는 필수';
    } else if (password.value.trim() === '') {
        warning.textContent = '비밀번호는 필수';
    } else {
        warning.textContent = '';
    }
    writeLog(warning.textContent === '' ? '입력 확인' : warning.textContent);
}
document.getElementById('check').addEventListener('click', checkInput);
