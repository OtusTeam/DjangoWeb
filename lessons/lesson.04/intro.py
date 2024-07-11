# Разница автоиматических тестов в ручных
from datetime import date
from journal import Article


article = Article(
    text='test text',
    author='some author',
    publish_date=date(2011, 2, 2),
)

# print(article)  # test text / some author / 2011-02-02


# Simple autotest
assert 2 > 1

assert 'test text / some author / 2011-02-02' == str(article),\
    f"test text / some author / 2011-02-02 != {str(article)}"
