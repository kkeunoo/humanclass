document.getElementById('same').addEventListener('click', function () {
    document.getElementById('deliveryName').value = this.checked
        ? document.getElementById('orderName').value : '';
    document.getElementById('deliveryAddress').value = this.checked
        ? document.getElementById('orderAddress').value : '';
});
document.getElementById('login').addEventListener('click', function () {
    const user = document.getElementById('user');
    const pw = document.getElementById('pw');
    const warning = document.getElementById('warning');
    if (user.value.trim() === '') warning.textContent = '아이디 필수';
    else if (pw.value.trim() === '') warning.textContent = '비밀번호 필수';
    else warning.textContent = '';
});
document.getElementById('pay').addEventListener('click', function () {
    const pizza = document.getElementById('pizza');
    const option = pizza.options[pizza.selectedIndex];
    const size = document.querySelector('[name="size"]:checked');
    const toppings = document.querySelectorAll('.topping:checked');
    const names = [];
    let total = Number(size.dataset.price);
    for (const topping of toppings) {
        names.push(topping.value);
        total += Number(topping.dataset.price);
    }
    const result = option.dataset.name + ' / ' + size.value +
        ' / ' + names.join(', ') + ' / ' + total + '원';
    document.getElementById('bill').textContent = result;
    console.log(result);
});
