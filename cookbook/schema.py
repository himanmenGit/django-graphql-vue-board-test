# cookbook/schema.py
import graphene

from cookbook.boards.schema import Query as BoardQuery


class Query(BoardQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)