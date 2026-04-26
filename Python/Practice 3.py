def trackPackages(transactions):
    stock = {}

    for transaction in transactions:
        action, package, quantity = transaction.split()
        quantity = int(quantity)

        if quantity < 0:
            return [-1]
        
        if action == "ship":
            if package not in stock or stock[package] < quantity:
                return [-1]
            stock[package] -= quantity
        elif action == "receive":
            stock[package] = stock.get(package, 0) + quantity

    result = []
    for package in sorted(stock):
        result.append(stock[package])

    return result

print(trackPackages([
    "receive box 10",
    "ship box 4",
    "receive crate 5"
]))