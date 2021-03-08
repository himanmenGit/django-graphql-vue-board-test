# app/schema.py
import graphene

from app.boards.schema import Query as BoardQuery
from app.boards.schema import Mutations as BoardMutation


class Query(BoardQuery, graphene.ObjectType):
    pass


class Mutations(BoardMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutations)
