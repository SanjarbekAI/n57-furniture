from django.db.models import Q
from django.views.generic import ListView, DetailView

from products.models import *


class ProductListView(ListView):
    template_name = 'shop/product-list.html'
    model = ProductModel
    context_object_name = "products"
    paginate_by = 1

    def get_queryset(self):
        products = ProductModel.objects.all()
        cat = self.request.GET.get('cat')
        size = self.request.GET.get('size')
        brand = self.request.GET.get('brand')
        color = self.request.GET.get('color')
        tag = self.request.GET.get('tag')
        q = self.request.GET.get('q')
        sort = self.request.GET.get('sort')
        if cat:
            products = products.filter(categories=cat)
        if size:
            products = products.filter(sizes__in=size)
        if brand:
            products = products.filter(brands=brand)
        if color:
            products = products.filter(colors=color)
        if tag:
            products = products.filter(tags=tag)
        if q:
            products = products.filter(
                Q(title__icontains=q) | Q(short_description__icontains=q)
            )
        if sort in ('title', '-title', 'price', '-price',):
            products = products.order_by(sort)

        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["colors"] = self.make_color_groups()
        context["categories"] = ProductCategoryModel.objects.all()
        context["tags"] = ProductTagModel.objects.all()
        context["brands"] = ProductManufactureModel.objects.all()
        context["sizes"] = ProductSizeModel.objects.all()
        return context

    @staticmethod
    def make_color_groups():
        colors = ProductColorModel.objects.all()
        result = list()
        temp_list = list()
        for color in colors:
            temp_list.append(color)
            if len(temp_list) == 2:
                result.append(temp_list)
                temp_list = []

        if len(temp_list) >= 1:
            result.append(temp_list)

        return result


class ProductDetailView(DetailView):
    template_name = 'shop/product-detail.html'
    model = ProductModel
    context_object_name = "product"


