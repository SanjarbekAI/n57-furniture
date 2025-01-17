from django.views.generic import ListView

from blogs.models import BlogModel, BlogCategoryModel


class BlogListView(ListView):
    template_name = 'blogs/blog-list.html'
    model = BlogModel
    context_object_name = 'blogs'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = BlogCategoryModel.objects.all()
        return context
