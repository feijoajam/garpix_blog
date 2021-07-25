from garpixcms.settings import *  # noqa

INSTALLED_APPS += [
    'garpix_blog',
]

GARPIX_BLOG_MIXIN = 'garpix_blog.mixins.EmptyMixin'
GARPIX_BLOG_POST_MIXIN = 'garpix_blog.mixins.EmptyMixin'
GARPIX_BLOG_POST_CATEGORY_MIXIN = 'garpix_blog.mixins.EmptyMixin'
GARPIX_BLOG_POST_IMAGE_MIXIN = 'garpix_blog.mixins.EmptyMixin'
GARPIX_BLOG_POST_VIDEO_MIXIN = 'garpix_blog.mixins.EmptyMixin'

MIGRATION_MODULES.update(
    {'garpix_blog': 'app.migrations.garpix_blog'}
)