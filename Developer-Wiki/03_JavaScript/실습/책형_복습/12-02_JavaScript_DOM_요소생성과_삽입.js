const log = document.getElementById('log');
const item = document.createElement('p');
item.textContent = '새 문장';
log.append(item);
log.append('<b>글자</b>');
log.append(item);
console.log(log.querySelectorAll('p').length);
console.log(log.textContent);
const rows = [['제목1', '작성자1'], ['제목2', '작성자2']];
const board = document.getElementById('board');
for (let i = 0; i < rows.length; i++) {
    const tr = document.createElement('tr');
    const title = document.createElement('td');
    const writer = document.createElement('td');
    title.textContent = rows[i][0];
    writer.textContent = rows[i][1];
    tr.append(title);
    tr.append(writer);
    board.append(tr);
}
console.log(board.querySelectorAll('tr').length);
console.log(board.querySelectorAll('tr')[0].querySelector('td').textContent);
console.log(board.querySelectorAll('tr')[1].querySelector('td').textContent);
