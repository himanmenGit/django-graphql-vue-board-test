from django.conf import settings
from django.db import models


class Board(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='게시판 이름')
    admin = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='관리자',
        related_name='boards',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{[self.pk]} {self.name} - {self.admin.username}'
