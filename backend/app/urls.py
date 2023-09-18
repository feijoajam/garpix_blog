from garpixcms.urls import *  # noqa
from django.urls import path, include


urlpatterns = \
    [
        path('', include(('garpix_blog.urls', 'blog'), namespace='garpix_blog')),
    ] + urlpatterns  # noqa
