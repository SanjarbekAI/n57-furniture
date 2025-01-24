from django import template

from orders.utils import get_products_in_cart

register = template.Library()


@register.filter
def in_cart(request, pk):
    return pk in request.session.get('cart', [])


@register.simple_tag
def get_user_cart(request):
    return get_products_in_cart(request)


@register.simple_tag
def get_product_count(request):
    return len(request.session.get('cart', []))


@register.simple_tag
def get_cart_total(request):
    products = get_products_in_cart(request)
    total = 0
    for product in products:
        total += product.price
    return total
