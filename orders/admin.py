# admin.py
from django.contrib import admin

from .models import OrderModel, OrderItemModel


class OrderItemInline(admin.StackedInline):  # Stacked inline for items
    model = OrderItemModel
    extra = 1  # Number of empty slots to show for adding new items
    readonly_fields = ('product_title', 'product_price')  # Optional: make fields read-only

    # Optional: prevent adding/removing items if needed
    can_delete = True
    show_change_link = True


@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]  # Include items inline

    # Customize order list display
    list_display = ('id', 'user', 'status', 'total_amount')
    list_filter = ('status',)
    search_fields = ('id', 'user__email', 'phone_number')


@admin.register(OrderItemModel)
class OrderItemAdmin(admin.ModelAdmin):
    # Separate admin for items if needed
    list_display = ('id', 'order', 'product_title', 'product_quantity')
    search_fields = ('product_title', 'order__id')
