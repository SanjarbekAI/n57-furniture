from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView

from orders.forms import CheckoutForm
from orders.models import OrderModel, OrderItemModel
from orders.utils import get_products_in_cart, calculate_total_price
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


class CheckoutTemplateView(LoginRequiredMixin, FormView):
    template_name = 'shop/product-checkout.html'
    form_class = CheckoutForm
    success_url = reverse_lazy("products:list")

    def form_valid(self, form):
        products = get_products_in_cart(request=self.request)
        if len(products) == 0:
            messages.info(self.request, "You do not have any products in your cart")
            return redirect(reverse_lazy("products:list"))

        order = OrderModel.objects.create(
            user=self.request.user,
            full_name=form.cleaned_data["full_name"],
            email=form.cleaned_data["email"],
            phone_number=form.cleaned_data["phone_number"],
            address=form.cleaned_data["address"],
            total_amount=calculate_total_price(products=products),
            total_products=len(products)
        )

        for product in products:
            OrderItemModel.objects.create(
                product=product,
                product_title=product.title,
                product_price=product.price,
                product_quantity=1,
                order=order
            )
        self.request.session["cart"] = []
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
