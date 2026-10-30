document.getElementById('xhr').addEventListener('click', function () {
    const xhr = new XMLHttpRequest();
    xhr.open('GET', 'book-users.json');
    xhr.onload = function () {
        const users = JSON.parse(xhr.responseText);
        console.log('XHR 응답', users[1].name);
        document.getElementById('result').textContent = users[1].name;
    };
    xhr.send();
    console.log('XHR 요청 뒤');
});
document.getElementById('fetch').addEventListener('click', function () {
    fetch('book-users.json', { method: 'GET' })
        .then(function (response) {
            return response.json();
        })
        .then(function (users) {
            console.log('fetch 응답', users[2].address.geo.lat);
            document.getElementById('result').textContent = users[2].address.geo.lat;
        })
        .catch(function (error) {
            document.getElementById('result').textContent = '읽기 실패';
            console.error(error);
        });
    console.log('fetch 요청 뒤');
});
