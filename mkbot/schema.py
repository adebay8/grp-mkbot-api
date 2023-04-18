import graphene
from graphene_django.debug import DjangoDebug
from stores.schema import schema as StoreSchema
from speech.schema import schema as SpeechSchema


class Query(StoreSchema.query, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name="_debug")


class Mutation(StoreSchema.mutation, SpeechSchema.mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
