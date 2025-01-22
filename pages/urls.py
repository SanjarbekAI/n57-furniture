from django.urls import path

from pages.views import home_page_view, ContactCreateView

app_name = "pages"

urlpatterns = [
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('', home_page_view, name='home')
]
