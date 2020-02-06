from google.cloud import language_v1 as language
import config


class LanguageClient:
    if config.USE_LANGUAGE_API:
        client = language.LanguageServiceClient()
    else:
        client = None
    DOCUMENT_TYPE_PLAIN_TEXT = 'PLAIN_TEXT'
    DOCUMENT_TYPE_HTML = 'HTML'

    @classmethod
    def get_entities(cls, content):
        response = cls.client.analyze_entities(dict(
            type=cls.DOCUMENT_TYPE_HTML,
            content=content,
        ))
        return [(e.name, e.salience) for e in response.entities]
