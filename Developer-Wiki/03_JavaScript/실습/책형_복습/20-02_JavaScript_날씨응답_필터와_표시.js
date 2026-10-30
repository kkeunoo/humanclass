const data = { response: { body: { items: { item: [
    { category: 'T1H', fcstTime: '0900', fcstValue: '25' },
    { category: 'REH', fcstTime: '0900', fcstValue: '70' },
    { category: 'RN1', fcstTime: '0900', fcstValue: '1' },
    { category: 'LGT', fcstTime: '0900', fcstValue: '0' },
    { category: 'T1H', fcstTime: '1000', fcstValue: '26' },
    { category: 'REH', fcstTime: '1000', fcstValue: '65' },
    { category: 'RN1', fcstTime: '1000', fcstValue: '0' }
] } } } };
const items = data.response.body.items.item;
const selected = items.filter(function (item) {
    return item.category === 'T1H' || item.category === 'REH' || item.category === 'RN1';
});
const groups = {};
for (const item of selected) {
    if (!groups[item.fcstTime]) groups[item.fcstTime] = {};
    groups[item.fcstTime][item.category] = item.fcstValue;
}
const times = Object.keys(groups).sort();
const rows = document.getElementById('rows');
rows.innerHTML = '';
for (const time of times) {
    const values = [time, groups[time].T1H, groups[time].REH, groups[time].RN1];
    const row = document.createElement('tr');
    for (const value of values) {
        const cell = document.createElement('td');
        cell.textContent = value === undefined ? '-' : value;
        row.append(cell);
    }
    rows.append(row);
    console.log(values.join(' | '));
}
console.log('원본 항목', items.length, '선택 항목', selected.length, '표 행', times.length);
