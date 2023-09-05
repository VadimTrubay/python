def discount_price(price, discount):
    def apply_discount():
        
        nonlocal price
        price = price - price*discount

    apply_discount()
    return price

