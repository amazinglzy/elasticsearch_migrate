from elasticsearch_dsl import Text, Date, Keyword
from elasticsearch_migrate.registry import Document, registry


@registry.register
class Page(Document):
    title = Text(fields={'raw': Keyword()})
    content = Text()
    refreshed_at = Date()

    class Index:
        name = 'page'
