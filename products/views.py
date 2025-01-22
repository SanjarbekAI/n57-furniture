from django.views.generic import TemplateView, ListView

from products.models import *


class ProductListView(ListView):
    template_name = 'shop/product-list.html'
    model = ProductModel
    context_object_name = "products"
    paginate_by = 1

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


class ProductDetailView(TemplateView):
    template_name = 'shop/product-detail.html'
