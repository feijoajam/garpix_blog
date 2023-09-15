from django.db import models
from garpix_blog.models.choice import Choice


class Vote(models.Model):
    user = models.ForeignKey('user.User', verbose_name='Пользователь', on_delete=models.SET_NULL,
                             blank=False, null=True, related_name='votes')
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name='votes')

    class Meta:
        verbose_name = 'Голос'
        verbose_name_plural = 'Голоса'

    def __str__(self):
        return f'{self.choice.poll.title[:15]} - {self.choice.title[:15]} - {self.user.name}'

    # def save(self, *args, **kwargs):
    #     just_created = not self.pk
    #     super().save(*args, **kwargs)
    #     if self.old_rating != self.rate or just_created:
    #         count_rating(self.book)
