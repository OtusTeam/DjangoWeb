from datetime import date
from journal import Article


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
