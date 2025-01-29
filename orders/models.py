"order as a uzum tezroq on ezma"

from django.contrib.auth import get_user_model
from django.db import models

from products.models import ProductModel

UserModel = get_user_model()


class OrderModel(models.Model):
    class OrderStatus(models.TextChoices):
        PENDING = "PENDING"
        ACCEPTED = "ACCEPTED"
        DELIVERING = "DELIVERING"
        DELIVERED = "DELIVERED"
        CANCELED = "CANCELED"

    user = models.ForeignKey(UserModel, on_delete=models.PROTECT, related_name="orders")
    phone_number = models.CharField(max_length=13)
    email = models.EmailField()
    full_name = models.CharField(max_length=128)
    address = models.CharField(max_length=255)

    total_products = models.PositiveSmallIntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(choices=OrderStatus, default=OrderStatus.PENDING, max_length=128)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "order"
        verbose_name_plural = "orders"


class OrderItemModel(models.Model):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(
        ProductModel, on_delete=models.SET_NULL,
        related_name="orders", null=True, blank=True
    )
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_title = models.CharField(max_length=255)
    product_quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.product.title

    def __repr__(self):
        return self.product.title

    class Meta:
        verbose_name = "order item"
        verbose_name_plural = "order items"
