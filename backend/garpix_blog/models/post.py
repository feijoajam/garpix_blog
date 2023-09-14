from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db import models
from django.utils.module_loading import import_string
from garpix_page.models import BasePage

from garpix_blog.mixins import PolymorphicActiveMixin
from garpix_utils.file import get_file_path

from garpix_blog.models import BlogPage
from garpix_blog.models.category_post import CategoryPost

PostMixin = import_string(settings.GARPIX_BLOG_POST_MIXIN)


class PostPage(BasePage, PostMixin, PolymorphicActiveMixin):
    short_description = models.TextField(default='', verbose_name='Краткое описание', blank=True)
    content = RichTextUploadingField(blank=True, default='', verbose_name='Контент поста')
    image = models.ImageField(verbose_name='Изображение', blank=True, null=True, upload_to=get_file_path)
    blog = models.ForeignKey(BlogPage, verbose_name='Проект', on_delete=models.CASCADE, related_name='posts')
    author = models.ForeignKey('user.User', verbose_name='Пользователь', on_delete=models.SET_NULL, blank=True,
                               null=True, related_name='posts')
    category = models.ForeignKey(CategoryPost, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ('-created_at',)
