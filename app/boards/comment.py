from django.conf import settings
from django.db import models

from .post import Post


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        verbose_name='작성글',
        related_name='comments',
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='작성자',
        related_name='comments',
        on_delete=models.CASCADE
    )

    content = models.CharField(max_length=1000, verbose_name='내용')
    created_date = models.DateField(auto_now_add=True, verbose_name='등록일')
    modified_date = models.DateField(auto_now=True, verbose_name='수정일')

    def __str__(self):
        return f'[{self.pk}] - {self.post.title} - {self.content} -{self.author.username}'
