const form = document.getElementById('form');
const query = document.getElementById('query');
const message = document.getElementById('message');
query.addEventListener('focus', function () {
    query.style.backgroundColor = 'yellow';
});
query.addEventListener('blur', function () {
    query.style.backgroundColor = '';
});
query.addEventListener('input', function () {
    console.log('입력', query.value);
});
form.addEventListener('submit', function (event) {
    event.preventDefault();
    const checked = query.value.trim();
    if (checked.length < 2) {
        message.textContent = '두 글자 이상 입력';
    } else {
        message.textContent = '검사 통과, 원래 값: [' + query.value + ']';
    }
    console.log(message.textContent);
});
