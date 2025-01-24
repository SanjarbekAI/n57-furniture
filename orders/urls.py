from django.urls import path

from orders.views import add_or_remove_cart

app_name = "orders"

urlpatterns = [
    path("add-or-remove-cart/<int:pk>/", add_or_remove_cart, name="add-or-remove-cart"),
    # path("add-or-remove-wishlist/<int:pk>/", add_or_remove_wishlist, name="add-or-remove-wishlist"),
    # path("show-cart/", show_cart, name="show-cart"),
    # path("show-wishlist/", show_wishlist, name="show-wishlist"),
]
