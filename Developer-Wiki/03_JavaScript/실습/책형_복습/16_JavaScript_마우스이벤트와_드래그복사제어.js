const drag = document.getElementById('drag');
let isDrag = false;
let offsetX = 0;
let offsetY = 0;
drag.addEventListener('mousedown', function (event) {
    isDrag = true;
    offsetX = event.offsetX;
    offsetY = event.offsetY;
    console.log('시작', offsetX, offsetY);
});
document.body.addEventListener('mousemove', function (event) {
    if (isDrag) {
        drag.style.left = event.pageX - offsetX + 'px';
        drag.style.top = event.pageY - offsetY + 'px';
    }
});
window.addEventListener('mouseup', function () {
    if (isDrag) {
        isDrag = false;
        console.log('끝', drag.style.left, drag.style.top);
    }
});
