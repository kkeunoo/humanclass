function makePayload(text) {
    return { username: '연습', content: text };
}
document.getElementById('preview').addEventListener('click', function () {
    const text = document.getElementById('prompt').value;
    const param = makePayload(text);
    const body = JSON.stringify(param);
    document.getElementById('result').textContent = body;
    console.log(typeof param, typeof body);
    console.log(body);
});
