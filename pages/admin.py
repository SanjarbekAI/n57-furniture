from django.contrib import admin

from pages.models import ContactModel


@admin.register(ContactModel)
class BlogCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'subject', 'created_at']
    search_fields = ['message', 'full_name']
    list_filter = ['created_at', 'email']
