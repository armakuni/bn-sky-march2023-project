from typing import List


class ShopItem:
    def __init__(self, id, name, unit_price):
        self.id = id
        self.name = name
        self.unit_price = unit_price


def calculate_cart_total(user_cart: List[ShopItem]=[]) -> float:
    cart_total_price = 0.0
    for item in user_cart:
        cart_total_price += item.unit_price

    return cart_total_price