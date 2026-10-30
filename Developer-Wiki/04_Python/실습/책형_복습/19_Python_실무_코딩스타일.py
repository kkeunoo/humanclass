def parse_order(line):
    parts = [part.strip() for part in line.split(',')]
    if len(parts) != 3:
        return None
    try:
        quantity = int(parts[1])
        price = int(parts[2].replace('원', ''))
    except ValueError:
        return None
    if quantity < 0 or price < 0 or price > 10000:
        return None
    return [parts[0], quantity, price]

def collect_orders(lines):
    accepted = []
    sales = 0
    for line in lines:
        order = parse_order(line)
        if order is None:
            continue
        accepted.append(order)
        sales += order[1] * order[2]
    return accepted, sales

rows = [' 사과 , 2, 3000원', '배, -1, 4000원', '귤, 3, 2000원']
orders, total = collect_orders(rows)
print(orders)
print(total)
