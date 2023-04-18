import graphene
from .models import Store, Category
from .types import CategoryType, StoreType


class Query(graphene.ObjectType):
    stores = graphene.List(StoreType, name=graphene.String())
    store = graphene.Field(StoreType, name=graphene.String(required=True))
    categories = graphene.List(CategoryType, name=graphene.String(required=False))

    def resolve_stores(root, info, **kwargs):
        if "name" in kwargs:
            try:
                return Store.objects.filter(name__icontains=kwargs.get("name"))
            except Store.DoesNotExist:
                return None
        return Store.objects.select_related("category").all()

    def resolve_store(root, info, **kwargs):
        try:
            return Store.objects.get(name__icontains=kwargs.get("name"))
        except Store.DoesNotExist:
            return None

    def resolve_categories(root, info, **kwargs):
        if "name" in kwargs:
            try:
                return Category.objects.filter(name__icontains=kwargs.get("name"))
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
