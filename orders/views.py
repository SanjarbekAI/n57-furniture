from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView

from orders.utils import get_products_in_cart
from products.models import ProductModel


def add_or_remove_cart(request, pk):
    cart = request.session.get('cart', [])

    if pk in cart:
        cart.remove(pk)
    else:
        cart.append(pk)
    request.session["cart"] = cart
    next_url = request.GET.get('next', reverse_lazy('products:list'))
    return redirect(next_url)


def add_or_remove_wishlist(request, pk):
    cart = request.session.get('wishlist', [])

    if pk in cart:
        cart.remove(pk)
    else:
        cart.append(pk)
    request.session["wishlist"] = cart
    next_url = request.GET.get('next', reverse_lazy('orders:wishlist'))
    return redirect(next_url)


class WishlistListView(ListView):
    template_name = 'shop/wishlist.html'
    context_object_name = "products"
    paginate_by = 1

    def get_queryset(self):
        wishlist = self.request.session.get('wishlist', [])
        products = []
        for pk in wishlist:
            product = ProductModel.objects.get(id=pk)
            products.append(product)
        return products


class CartListView(ListView):
    template_name = 'shop/product-cart.html'
    context_object_name = "products"

    def get_queryset(self):
        return get_products_in_cart(self.request)
