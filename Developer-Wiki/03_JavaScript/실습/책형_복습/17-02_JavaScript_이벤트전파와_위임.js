document.getElementById('parent').addEventListener('click', function (event) {
    console.log('부모', event.target.id, event.currentTarget.id);
});
document.getElementById('child1').addEventListener('click', function (event) {
    event.stopPropagation();
    console.log('자식1');
});
const board = document.getElementById('board');
board.addEventListener('click', function (event) {
    if (event.target.classList.contains('title')) {
        console.log('제목', event.target.textContent);
    }
    if (event.target.hasAttribute('writer')) {
        console.log('작성자', event.target.getAttribute('writer'));
    }
});
board.querySelector('input.chk').addEventListener('click', function (event) {
    event.stopPropagation();
    const row = this.parentNode.parentNode;
    console.log('체크', this.checked, row.querySelector('.title').textContent);
});
