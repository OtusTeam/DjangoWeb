from pytest import fixture
from datetime import date
from journal.article import Article


@fixture
def other_article():
    return Article(
            text='test text 1',
            author='some author',
            publish_date=date(2011, 2, 2),
        )
