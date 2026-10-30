const area = document.getElementById('area');
function makeCopyText(selection) {
    return selection + '[출처] www.naver.com';
}
document.getElementById('preview').addEventListener('click', function () {
    const result = makeCopyText('복사 연습');
    document.getElementById('result').textContent = result;
    console.log(result);
});
area.addEventListener('copy', function (event) {
    event.preventDefault();
    const selection = window.getSelection().toString();
    if (selection.length === 0) return;
    event.clipboardData.setData('text/plain', makeCopyText(selection));
});
window.addEventListener('resize', function () {
    document.getElementById('size').textContent =
        '가로 ' + window.innerWidth + ', 세로 ' + window.innerHeight;
});
