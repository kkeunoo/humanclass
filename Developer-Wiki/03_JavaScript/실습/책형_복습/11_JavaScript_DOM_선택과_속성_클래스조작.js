const title = document.getElementById('book-title');
console.log(title.textContent);
const notes = document.querySelectorAll('#panel .note');
console.log(notes.length);
console.log(notes[0].textContent);
console.log(document.querySelector('.missing'));
const missing = document.querySelectorAll('.missing');
console.log(missing.length);
if (missing) {
    console.log('목록 객체 있음');
}
