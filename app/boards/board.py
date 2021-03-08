from django.conf import settings
from django.db import models
from django.utils.text import slugify


class Board(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='게시판 이름')
    slug = models.SlugField(max_length=100, unique=True, null=True, verbose_name='게시판 별명')
    admin = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='관리자',
        related_name='boards',
        on_delete=models.CASCADE
    )

    def save(self, *args, **kwargs):
        # if not self.slug:
        self.slug = slugify(self.name)
        super(Board, self).save(*args, **kwargs)

    def __str__(self):
        return f'{[self.pk]} {self.name} - {self.admin.username}'
