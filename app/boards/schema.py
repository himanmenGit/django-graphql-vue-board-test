import graphene
from django.contrib.auth import get_user_model
from graphene_django.types import DjangoObjectType

from .board import Board
from .post import Post
from .comment import Comment

User = get_user_model()


class BoardType(DjangoObjectType):
    class Meta:
        model = Board
        fields = '__all__'


class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = ('title', 'content', 'board', 'author')


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment
        fields = '__all__'


class UserType(DjangoObjectType):
    class Meta:
        model = User


class Query:
    board_detail = graphene.Field(
        BoardType,
        id=graphene.Int(),
        name=graphene.String()
    )
    all_boards = graphene.List(BoardType)

    def resolve_all_boards(self, info):
        return Board.objects.all()

    def resolve_board_detail(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Board.objects.get(pk=id)

        if name is not None:
            return Board.objects.get(name=name)

        return None

    post_detail = graphene.Field(
        PostType,
        id=graphene.Int(),
        title=graphene.String()
    )

    all_posts = graphene.List(PostType, board_name=graphene.String())

    def resolve_all_posts(self, info, **kwargs):
        return Post.objects.filter(board__name=kwargs.get('board_name'))

    def resolve_post_detail(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Board.objects.get(pk=id)

        return None

    comment_detail = graphene.Field(
        CommentType,
        id=graphene.Int(),
        content=graphene.String()
    )
    all_comments = graphene.List(CommentType)

    def resolve_all_comments(self, info, **kwargs):
        return Comment.objects.filter(post_id=kwargs.get('post_id'))

    def resolve_comment_detail(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Board.objects.get(pk=id)

        return None


class BoardCreateMutations(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    board = graphene.Field(BoardType)

    def mutate(self, info, **kwargs):
        board = Board.objects.create(name=kwargs.get('name'), admin_id=1)
        return BoardCreateMutations(board=board)


class PostCreateMutations(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        content = graphene.String(required=True)
        board = graphene.ID(required=True)
        author = graphene.ID(required=True)

    post = graphene.Field(PostType)

    def mutate(self, info, **kwargs):
        post = Post.objects.create(
            title=kwargs.get('title'),
            content=kwargs.get('content'),
            board_id=kwargs.get('board'),
            author_id=kwargs.get('author')
        )
        return PostCreateMutations(post=post)


class PostUpdateMutations(graphene.Mutation):
    class Arguments:
        pk = graphene.ID(required=True)
        title = graphene.String()
        content = graphene.String()
        board = graphene.ID()
        author = graphene.ID()

    post = graphene.Field(PostType)

    def mutate(self, info, **kwargs):
        post = Post.objects.get(pk=kwargs.get('pk'))
        post.title = kwargs.get('title') if kwargs.get('title') else post.title
        post.content = kwargs.get('content') if kwargs.get('content') else post.content
        post.board_id = kwargs.get('board') if kwargs.get('board') else post.board.id
        post.author_id = kwargs.get('author') if kwargs.get('author') else post.author.id
        post.save()

        return PostUpdateMutations(post=post)


class PostDeleteMutations(graphene.Mutation):
    class Arguments:
        pk = graphene.ID(required=True)

    post = graphene.Field(PostType)

    def mutate(self, info, **kwargs):
        post = Post.objects.get(pk=kwargs.get('pk'))
        post.is_delete = True
        post.save()

        return PostDeleteMutations(post=post)


class Mutations(graphene.ObjectType):
    create_board = BoardCreateMutations.Field()
    create_post = PostCreateMutations.Field()
    update_post = PostUpdateMutations.Field()
    delete_post = PostDeleteMutations.Field()
