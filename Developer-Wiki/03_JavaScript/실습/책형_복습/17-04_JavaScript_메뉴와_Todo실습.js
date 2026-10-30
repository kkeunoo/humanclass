const menuButtons = document.querySelectorAll('#menu button');
for (const button of menuButtons) {
    button.addEventListener('click', function () {
        for (const item of menuButtons) item.classList.remove('selected');
        this.classList.add('selected');
    });
}
const list = document.getElementById('list');
const all = document.getElementById('all');
function syncAll() {
    const checks = list.querySelectorAll('.chk');
    const checked = list.querySelectorAll('.chk:checked');
    all.checked = checks.length > 0 && checks.length === checked.length;
}
function paintRow(check) {
    const text = check.parentNode.querySelector('span');
    if (check.checked) text.classList.add('done');
    else text.classList.remove('done');
}
document.getElementById('add').addEventListener('click', function () {
    const input = document.getElementById('todo');
    const warning = document.getElementById('warning');
    if (input.value.trim() === '') {
        warning.textContent = '한 글자 이상 입력';
        return;
    }
    warning.textContent = '';
    const row = document.createElement('div');
    row.classList.add('row');
    const check = document.createElement('input');
    check.type = 'checkbox';
    check.classList.add('chk');
    check.setAttribute('aria-label', '할 일 선택');
    const text = document.createElement('span');
    text.textContent = input.value.trim();
    const del = document.createElement('button');
    del.type = 'button';
    del.textContent = '삭제';
    del.addEventListener('click', function () {
        row.remove();
        syncAll();
    });
    check.addEventListener('click', function () {
        paintRow(check);
        syncAll();
    });
    row.append(check, text, del);
    list.prepend(row);
    input.value = '';
    syncAll();
});
all.addEventListener('click', function () {
    const checks = list.querySelectorAll('.chk');
    for (const check of checks) {
        check.checked = this.checked;
        paintRow(check);
    }
    syncAll();
});
document.getElementById('deleteSelected').addEventListener('click', function () {
    const checks = list.querySelectorAll('.chk:checked');
    for (const check of checks) check.parentNode.remove();
    syncAll();
});
