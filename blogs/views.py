from django.views.generic import ListView

from blogs.models import BlogModel


class BlogListView(ListView):
    template_name = 'blog-list-sidebar-left.html'
    model = BlogModel
    context_object_name = 'blogs'
