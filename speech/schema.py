import graphene
from .helpers import SpeechTextConverter


class GetStoreFromSpeech(graphene.Mutation):
    class Arguments:
        uri = graphene.String()

    store = graphene.String()

    def mutate(root, info, uri):
        converter = SpeechTextConverter(uri=uri)
        # transcription = converter.transcribe_speech()
        # tokens = converter.tokenize_text("Take me to bed")
        entities = converter.get_entities("Take me to hmv")
        entity_names = list(entities.keys())
        entity_types = list(entities.values())
        store_name = entity_names[entity_types.index("ORGANIZATION")]

        return GetStoreFromSpeech(store=store_name)


class Mutation(graphene.ObjectType):
    getStoreFromSpeech = GetStoreFromSpeech.Field()


schema = graphene.Schema(mutation=Mutation)
