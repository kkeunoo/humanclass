const game = document.getElementById('game');
game.style.left = '10px';
game.style.top = '20px';
document.body.addEventListener('keydown', function (event) {
    let changed = true;
    if (event.keyCode === 39) game.style.left = parseInt(game.style.left) + 10 + 'px';
    else if (event.keyCode === 37) game.style.left = parseInt(game.style.left) - 10 + 'px';
    else if (event.keyCode === 40) game.style.top = parseInt(game.style.top) + 10 + 'px';
    else if (event.keyCode === 38) game.style.top = parseInt(game.style.top) - 10 + 'px';
    else changed = false;
    if (changed) console.log(game.style.left, game.style.top);
});
document.getElementById('user').addEventListener('keyup', function (event) {
    if (event.keyCode === 13) document.getElementById('pw').focus();
});
document.getElementById('pw').addEventListener('keyup', function (event) {
    if (event.keyCode === 13) document.getElementById('check').click();
});
document.getElementById('check').addEventListener('click', function () {
    console.log('연습 확인');
});
window.addEventListener('scroll', function () {
    document.getElementById('position').textContent = window.scrollY;
});
document.getElementById('top').addEventListener('click', function () {
    window.scrollTo({ top: 0, behavior: 'smooth' });
});
