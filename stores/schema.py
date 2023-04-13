import graphene
from graphene_django import DjangoObjectType
from .models import Store, Category


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = "__all__"


class StoreType(DjangoObjectType):
    class Meta:
        model = Store
        fields = "__all__"


class Query(graphene.ObjectType):
    stores = graphene.List(StoreType)
    categories = graphene.List(CategoryType, name=graphene.String(required=False))

    def resolve_stores(root, info):
        return Store.objects.select_related("category").all()

    def resolve_categories(root, info, **kwargs):
        if "name" in kwargs:
            try:
                return Category.objects.filter(name=kwargs.get("name"))
            except Category.DoesNotExist:
                return None

        return Category.objects.all()


class AddCategory(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        external_id = graphene.Int()

    status = graphene.Boolean()
    category = graphene.Field(CategoryType)

    def mutate(parent, info, **kwargs):
        status = True
        category = Category(**kwargs)
        category.save()

        return AddCategory(status=status, category=category)


class AddStore(graphene.Mutation):
    status = graphene.Boolean()

    def mutate(root, info):
        return AddStore(status=True)


class Mutation(graphene.ObjectType):
    addCategory = AddCategory.Field()
    addStore = AddStore.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
