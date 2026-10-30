const form = document.getElementById('todoForm');
const input = document.getElementById('todoInput');
const list = document.getElementById('list');
const count = document.getElementById('count');
const warning = document.getElementById('warning');
function updateCount() {
    count.textContent = list.querySelectorAll('li').length;
}
form.addEventListener('submit', function (event) {
    event.preventDefault();
    const title = input.value.trim();
    if (title === '') {
        warning.textContent = '내용을 입력하세요';
        return;
    }
    warning.textContent = '';
    const row = document.createElement('li');
    const text = document.createElement('span');
    text.textContent = title;
    const removeButton = document.createElement('button');
    removeButton.type = 'button';
    removeButton.textContent = '삭제';
    removeButton.addEventListener('click', function () {
        row.remove();
        updateCount();
    });
    row.append(text, removeButton);
    list.append(row);
    input.value = '';
    updateCount();
});
