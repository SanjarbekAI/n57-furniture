from django import template

from orders.utils import get_products_in_cart, calculate_total_price

register = template.Library()


@register.filter
def in_cart(request, pk):
    return pk in request.session.get('cart', [])

@register.filter
def in_wishlist(request, pk):
    return pk in request.session.get('wishlist', [])


@register.simple_tag
def get_user_cart(request):
    return get_products_in_cart(request)


@register.simple_tag
def get_product_count(request):
    return len(request.session.get('cart', []))


@register.simple_tag
def get_cart_total(request):
    products = get_products_in_cart(request)
    return calculate_total_price(products=products)
