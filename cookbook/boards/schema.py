import graphene
from graphene_django.types import DjangoObjectType

from .board import Board
from .post import Post
from .comment import Comment


class BoardType(DjangoObjectType):
    class Meta:
        model = Board


class PostType(DjangoObjectType):
    class Meta:
        model = Post


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment


class Query:
    board = graphene.Field(
        BoardType,
        id=graphene.Int(),
        name=graphene.String()
    )
    all_boards = graphene.List(BoardType)

    def resolve_all_boards(self, info, **kwargs):
        return Board.objects.all()

    def resolve_board(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Board.objects.get(pk=id)

        if name is not None:
            return Board.objects.get(name=name)

        return None

    post = graphene.Field(
        PostType,
        id=graphene.Int(),
        title=graphene.String()
    )

    all_posts = graphene.List(PostType)

    def resolve_all_posts(self, info, **kwargs):
        return Post.objects.all()

    def resolve_post(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Board.objects.get(pk=id)

        return None

    comment = graphene.Field(
        CommentType,
        id=graphene.Int(),
        content=graphene.String()
    )
    all_comments = graphene.List(CommentType)

    def resolve_all_comments(self, info, **kwargs):
        return Comment.objects.all()

    def resolve_comment(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Board.objects.get(pk=id)

        return None

# chema = graphene.Schema(query=Query)
