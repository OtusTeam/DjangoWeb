from .article import Article


def reverse_list(self, iterable):
    return reversed(iterable)


class Journal:

    def __init__(self, name, articles=None):
        self.name = name
        self._articles = articles or []
        # self.reverse_list()
        # Journal.reverse_list()

    def __len__(self):
        return len(self._articles)

    def add(self, article: Article):
        self._articles.append(article)

    def __bool__(self):
        return bool(self._articles)

    def __getitem__(self, item):
        return self._articles[item]

    def __add__(self, other):
        return Journal(
            name=self.name + other.name,
            articles=self._articles + other._articles
        )

    @staticmethod
    def reverse_list(iterable):
        return reversed(iterable)
