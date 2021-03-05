from django.conf import settings
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='제목')
    content = models.CharField(max_length=1000, verbose_name='내용')

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='작성자',
        related_name='posts',
        on_delete=models.CASCADE
    )

    created_date = models.DateField(auto_now_add=True, verbose_name='등록일')
    modified_date = models.DateField(auto_now=True, verbose_name='수정일')

    def __str__(self):
        return f'[{self.pk}] - {self.title}, {self.author.username}'
