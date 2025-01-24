from django.shortcuts import redirect
from django.urls import reverse_lazy


def add_or_remove_cart(request, pk):
    cart = request.session.get('cart', [])

    if pk in cart:
        cart.remove(pk)
    else:
        cart.append(pk)
    request.session["cart"] = cart
    next_url = request.GET.get('next', reverse_lazy('products:list'))
    return redirect(next_url)
