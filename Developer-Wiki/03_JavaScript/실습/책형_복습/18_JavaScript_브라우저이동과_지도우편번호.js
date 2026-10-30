document.getElementById('move').addEventListener('click', function () {
    location.href = '#practice';
    console.log('같은 문서 이동');
    console.log(location.href.split('#')[1]);
});
function showAddress(data) {
    const text = data.address + ' / ' + data.zonecode;
    document.getElementById('address').textContent = text;
    console.log(text);
}
document.getElementById('sample').addEventListener('click', function () {
    showAddress({ address: '연습시 학습로 1', zonecode: '00000' });
});
