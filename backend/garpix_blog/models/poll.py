from django.db import models
from garpix_page.models import BasePage
from garpix_blog.mixins import PolymorphicActiveMixin


class Poll(BasePage, PolymorphicActiveMixin):
    author = models.ForeignKey('user.User', verbose_name='Пользователь', on_delete=models.CASCADE, blank=True,
                               null=True, related_name='polls')

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    def __str__(self):
        return self.title

    # TODO: add this to celery
    def update_percents(self):
        from garpix_blog.models import Choice
        all_choices = Choice.objects.filter(poll=self)
        sum_ = sum([x.cnt_votes for x in all_choices])
        for choice in all_choices:
            percent = choice.cnt_votes / sum_
            choice.percent = round(percent * 100)
        Choice.objects.bulk_update(all_choices, ['percent'])
