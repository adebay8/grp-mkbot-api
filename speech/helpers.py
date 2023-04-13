from google.cloud import speech, language_v1


class SpeechTextConverter:
    def __init__(self, uri):
        self.audio_uri = uri

    def transcribe_speech(self):
        client = speech.SpeechClient()
        audio = speech.RecognitionAudio(uri=self.audio_uri)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code="en-US",
        )
        response = client.recognize(config=config, audio=audio)

        transcription = [
            result.alternatives[0].transcript for result in response.results
        ]

        return transcription

    def tokenize_text(self, text):
        client = language_v1.LanguageServiceClient()

        language = "en"
        type_ = language_v1.Document.Type.PLAIN_TEXT
        document = {"content": text, "type_": type_, "language": language}

        encoding_type = language_v1.EncodingType.UTF8

        response = client.analyze_syntax(
            request={"document": document, "encoding_type": encoding_type}
        )

        word_pos_mapping = {}

        for token in response.tokens:
            pos = language_v1.PartOfSpeech.Tag(token.part_of_speech.tag).name
            word_pos_mapping[token.text.content] = pos

        return word_pos_mapping

    def get_entities(self, text):
        client = language_v1.LanguageServiceClient()

        type_ = language_v1.Document.Type.PLAIN_TEXT
        language = "en"
        document = {"content": text, "type_": type_, "language": language}

        encoding_type = language_v1.EncodingType.UTF8

        response = client.analyze_entities(
            request={"document": document, "encoding_type": encoding_type}
        )

        word_entity_mapping = {}

        for entity in response.entities:
            word_entity_mapping[entity.name] = language_v1.Entity.Type(
                entity.type_
            ).name

        return word_entity_mapping
