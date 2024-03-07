from shopping_carts.models import ShoppingCart


def get_total_sum(cart: ShoppingCart):
    products_in_cart = cart.productincart_set.all()
    total_sum = 0
    for product in products_in_cart:
        total_sum += product.product.price * product.count

    cart.total_sum = total_sum
    cart.save()
