const box = document.getElementById('box');
console.log(`인라인=[${box.style.height}]`);
const height = getComputedStyle(box).getPropertyValue('height');
console.log(height);
box.style.height = parseInt(height) + 5 + 'px';
console.log(box.style.height);
const quizzes = document.querySelectorAll('.quiz');
let count = 0;
for (let i = 0; i < quizzes.length; i++) {
    if (quizzes[i].classList.contains('q2')) {
        count++;
    }
    if (quizzes[i].textContent.trim() === '') {
        quizzes[i].textContent = '비어있음';
    }
}
console.log(count);
console.log(quizzes[1].textContent);
