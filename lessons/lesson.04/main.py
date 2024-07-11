from datetime import date
from journal import Article, Journal, NewsArticle


python_article = Article(
    'Python is Cool',
    'Leo',
    date(2024, 7, 8)
)

print(str(python_article))
print(repr(python_article))
print(python_article)

print(len(python_article))

java_article = Article(
    'Java is Cool too',
    'Leo',
    date(2024, 7, 9)
)

print(python_article == java_article)
print(python_article == python_article)

print(python_article is java_article)

python_article_the_same = Article(
    'Python is Cool',
    'Leo',
    date(2024, 7, 8)
)

print(python_article == python_article_the_same)

python_article()
java_article()

journal = [
    python_article,
    java_article,
]

# for article in journal:
#     print(article)

# journal_iterator = iter(journal)
# print(journal_iterator)
# print(next(journal_iterator))
# print(next(journal_iterator))
# print(next(journal_iterator))

journal = Journal(
    name='Be good developer'
)

# print(len(journal))

journal.add(python_article)
journal.add(java_article)

# print(len(journal))

# print(journal[0])
#
# for article in journal:
#     print(article)
#
# journal_iterator = iter(journal)
# print(next(journal_iterator))

# Проверка на пустой журнал
# print(
#     len(journal) == 0
# )

empty_journal = Journal(
    'empty',
)

# print(
#     len(empty_journal) == 0
# )

if journal:
    print('Не пустой')

if empty_journal:
    print('Пустой')

print(bool(journal))
print(bool(empty_journal))

empty_journal.add(python_article)
print(bool(empty_journal))

# j = [
#     1,
#     2,
# ]
#
# e = [
#     3,
#     4,
# ]
#
# r = j + e
# print(r)
#
# j += e
# print(j)

result = journal + empty_journal
print(len(result))
print(result.name)

# journal += empty_journal

# print(journal.name)

sorted_journal = sorted(journal, reverse=True)

print(sorted_journal)

sorted_journal = sorted(journal, key=lambda article: article.publish_date)
sorted_journal = sorted(journal, key=lambda article: article.publish_date, reverse=True)

print(sorted_journal)

current_news_article = Article.create_article(
    'News',
    'Bill',
)

print(current_news_article)
print(type(current_news_article))

news_article = NewsArticle.create_article(
    'But new class',
    'Kate',
)

print(type(news_article))
