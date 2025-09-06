


def calculate_total(cart: list[tuple]) -> float: 
    total = 0.0
    for price, quantity in cart:
        total += price * quantity
    return total


def apply_discount(total: float, discount_rate: float =0.0) -> float:
    return total * (1 + discount_rate)

def print_total_amount(total):
    print(f"Total ${total:.2f}") 

def main():
    cart = [(100, 2), (250, 1), (50, 4)]
    
    total = calculate_total(cart)
    total = apply_discount(total, 0.1)
    print_total_amount(total)


if __name__ == "__main__":
    main()