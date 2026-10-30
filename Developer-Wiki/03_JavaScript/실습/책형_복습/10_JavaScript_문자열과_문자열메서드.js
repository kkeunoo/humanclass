function maskEmail(email) {
    const pos = email.indexOf('@');
    if (pos < 1) {
        return '이메일을 확인하세요';
    }
    const id = email.slice(0, pos);
    let stars = '';
    for (let i = 2; i < id.length; i++) {
        stars += '*';
    }
    return id.slice(0, 2) + stars + email.slice(pos);
}
console.log(maskEmail('abcd@example.com'));
console.log(maskEmail('abcd'));
const word = '사과 주스';
console.log(word.replace('사과', '포도'));
console.log(word);
