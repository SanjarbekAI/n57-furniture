from django.contrib import admin

from .models import (
    ProductCategoryModel,
    ProductTagModel,
    ProductSizeModel,
    ProductManufactureModel,
    ProductColorModel,
    ProductModel,
    ProductCommentModel, ProductImageModel
)


@admin.register(ProductCategoryModel)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')
    search_fields = ('title',)
    list_filter = ('parent',)


@admin.register(ProductTagModel)
class ProductTagAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(ProductSizeModel)
class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(ProductManufactureModel)
class ProductManufactureAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo')
    search_fields = ('name',)


@admin.register(ProductColorModel)
class ProductColorAdmin(admin.ModelAdmin):
    list_display = ('title', 'code')
    search_fields = ('title', 'code')


class ProductImageAdmin(admin.StackedInline):
    model = ProductImageModel


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'in_stock', 'quantity', 'discount', 'discount_price', 'sku')
    search_fields = ('title', 'sku')
    list_filter = ('in_stock', 'categories', 'brands')
    filter_horizontal = ('colors', 'sizes', 'tags', 'categories')
    inlines = [ProductImageAdmin]


@admin.register(ProductCommentModel)
class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'comment')
    search_fields = ('user__username', 'product__title', 'comment')
