import json

import products
from cart import dao
from products import Product


class Cart:
    def __init__(self, id: int, username: str, contents: list[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    def load(data):
        return Cart(data['id'], data['username'], data['contents'], data['cost'])

def get_cart(username: str) -> list[Product]:
    try:
        cart_details = dao.get_cart(username)
        if not cart_details:
            return []

        product_ids = []
        for cart_detail in cart_details:
            contents = cart_detail.get('contents', "[]")
            if contents:
                product_ids.extend(json.loads(contents))

        return [products.get_product(product_id) for product_id in product_ids]
    except Exception as e:
        print(f"Error retrieving cart for username '{username}': {e}")
        return []


def add_to_cart(username: str, product_id: int):
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    dao.remove_from_cart(username, product_id)

def delete_cart(username: str):
    dao.delete_cart(username)


