const list = { contents: [] };
function appendLine(role, text) {
    const line = document.createElement('p');
    line.textContent = role + ': ' + text;
    document.getElementById('result').append(line);
}
document.getElementById('add').addEventListener('click', function () {
    const prompt = document.getElementById('prompt').value;
    list.contents.push({ role: 'user', parts: [{ text: prompt }] });
    const body = JSON.stringify(list);
    console.log('요청 직전 항목', list.contents.length);
    console.log(typeof body);
    // 실제 AI 응답이 아닌, 구조 풀이용 가상 응답
    const result = { candidates: [{ content: { parts: [{ text: '연습 답변' }] } }] };
    const answer = result.candidates[0].content.parts[0].text;
    list.contents.push({ role: 'model', parts: [{ text: answer }] });
    appendLine('user', prompt);
    appendLine('model', answer);
    console.log('답변 기록 뒤 항목', list.contents.length);
});
