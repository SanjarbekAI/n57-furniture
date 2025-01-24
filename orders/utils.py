from products.models import ProductModel


def get_products_in_cart(request):
    cart = request.session.get('cart', [])
    products = []
    for pk in cart:
        product = ProductModel.objects.get(pk=pk)
        products.append(product)
    return products