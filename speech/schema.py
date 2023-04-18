import graphene
from .helpers import SpeechTextConverter
from stores.schema import StoreType
from stores.models import Store


class GetStoreFromSpeech(graphene.Mutation):
    class Arguments:
        uri = graphene.String(required=True)

    store = graphene.Field(StoreType)

    def mutate(root, info, **kwargs):
        uri = kwargs.get("uri")
        converter = SpeechTextConverter()
        transcription = converter.transcribe_speech(uri=uri)

        if transcription is None or len(transcription) < 1:
            raise Exception("unable to transcribe the speech")

        entities = converter.get_entities(transcription[0])
        entity_names = list(entities.keys())
        entity_types = list(entities.values())

        print(transcription)
        print(entities)

        if len(entity_names) < 1:
            raise Exception("unable to detect store from speech")

        store_name = entity_names[entity_types.index("ORGANIZATION")]
        store = Store.objects.get(name__icontains=store_name)

        return GetStoreFromSpeech(store=store)


class Mutation(graphene.ObjectType):
    getStoreFromSpeech = GetStoreFromSpeech.Field()


schema = graphene.Schema(mutation=Mutation)
