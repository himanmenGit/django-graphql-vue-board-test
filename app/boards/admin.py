from django.contrib import admin
from .board import Board
from .post import Post
from .comment import Comment

admin.site.register(Board)
admin.site.register(Post)
admin.site.register(Comment)
