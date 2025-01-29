from products.models import ProductModel


def get_products_in_cart(request):
    cart = request.session.get('cart', [])
    products = []
    for pk in cart:
        product = ProductModel.objects.get(pk=pk)
        products.append(product)
    return products


def calculate_total_price(products):
    total = 0
    for product in products:
        total += product.price
    return total