products = ["笔记本电脑", "键盘", "鼠标", "显示器", "耳机"]
prices = [5999, 299, 89, 1999, 599]

price_list = [(i, product, price) for i, (product, price) in enumerate(zip(products, prices))]
for i, product, price in price_list:
    print(f"{i+1}. {product} - ¥{price}元")

product_dict = {product : price for product, price in zip(products, prices)}
new_product = {product : price for product, price in product_dict.items() if price > 500}

records = [
    {"id": 1, "name": "Alice", "score": 92},
    {"id": 2, "name": "Bob", "score": 78},
    {"id": 3, "name": "Charlie", "score": 85},
    {"id": 4, "name": "Diana", "score": 95},
]
excellent_student = [dict.get("name", "Unknown") for dict in records if dict.get("score", 0) >= 85]
print(excellent_student)