def cost_delivery(quantity, *_, discount=0):
    sum_delivery = (quantity - 1)*2 + 5
    sum_discount = sum_delivery * discount
    return sum_delivery - sum_discount

print(cost_delivery(5, discount=1))
