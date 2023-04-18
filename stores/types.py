from .models import Store, Category, StoreNode
from graphene_django import DjangoObjectType


class StoreNodeType(DjangoObjectType):
    class Meta:
        model = StoreNode
        fields = "__all__"


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = "__all__"


class StoreType(DjangoObjectType):
    class Meta:
        model = Store
        fields = "__all__"
