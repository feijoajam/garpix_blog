from garpix_blog.models import BlogPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(BlogPage)
class BlogPageAdmin(BasePageAdmin):

    def has_module_permission(self, request):
        return True
