from django.urls import path

from orders.views import add_or_remove_cart, WishlistListView, add_or_remove_wishlist, CartListView, \
    CheckoutTemplateView

app_name = "orders"

urlpatterns = [
    path("add-or-remove-cart/<int:pk>/", add_or_remove_cart, name="add-or-remove-cart"),
    path("add-or-remove-wishlist/<int:pk>/", add_or_remove_wishlist, name="add-or-remove-wishlist"),
    path("cart/", CartListView.as_view(), name="cart"),
    path("wishlist/", WishlistListView.as_view(), name="wishlist"),
    path("checkout/", CheckoutTemplateView.as_view(), name="checkout"),
]
