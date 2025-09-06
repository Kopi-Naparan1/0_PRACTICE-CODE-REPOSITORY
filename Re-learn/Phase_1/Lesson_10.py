products = [
    {"name": "Apple", "price": 50, "stock": 100},
    {"name": "Banana", "price": 30, "stock": 150}
]


product_names: list = [item["name" ]for item in products]
product_total_value: dict[str, int] = {item["name"]: item["price"] * item["stock"] if item["stock"] > 120 * .9 else item["price"] * item["stock"] for item in products}
unique_prices: set = {item["price"] for item in products}


for product in products:

    print(f"Product: {product["name"]}, Stock: {product["stock"]}, Total value: $ {product["stock"] * product["price"]} ")