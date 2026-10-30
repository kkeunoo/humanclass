const person = {
    name: '민지',
    age: 20,
    detail: { 'study-year': 1 },
    greet: function () { console.log('안녕'); }
};
console.log(person.name);
console.log(person.detail['study-year']);
person.age = 21;
person.city = '서울';
person.greet();
const text = JSON.stringify(person);
console.log(typeof text);
console.log(text);
const restored = JSON.parse(text);
console.log(restored.age);
console.log(typeof restored.greet);
console.log(Object.keys(restored).join(', '));
delete restored.city;
console.log(restored.city);
const students = [{ name: '민지' }, { name: '준호' }];
for (const student of students) console.log(student.name);
