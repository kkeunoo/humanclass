text = '사과, 2, 3000원\n귤, 3, 2000\n우유, 1, -2000\n주스, 1, 12000\n잘못된줄\n물, 여러개, 1000\n'
with open('book_orders.txt', 'w', encoding='utf-8') as file:
    file.write(text)
orders = []
total = 0
skipped = 0
with open('book_orders.txt', 'r', encoding='utf-8') as file:
    for line in file:
        if not line.strip():
            continue
        parts = [part.strip() for part in line.split(',')]
        if len(parts) != 3:
            skipped += 1
            continue
        try:
            quantity = int(parts[1])
            price = int(parts[2].replace('원', ''))
        except ValueError:
            skipped += 1
            continue
        if quantity >= 0 and 0 <= price <= 10000:
            orders.append([parts[0], quantity, price])
            total += quantity * price
        else:
            skipped += 1
print(orders)
print(total)
print('제외', skipped)
