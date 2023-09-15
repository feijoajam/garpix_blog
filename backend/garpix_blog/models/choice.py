from django.db import models
from garpix_blog.models.poll import Poll


class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='choices')
    title = models.CharField(max_length=200)
    cnt_votes = models.IntegerField(default=0)
    percent = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Варианты'
        verbose_name_plural = 'Варианты'

    def __str__(self):
        return self.title

    def upvote(self):
        self.cnt_votes += 1
        self.save()

    def downvote(self):
        self.cnt_votes -= 1
        self.save()
