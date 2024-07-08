class Article:

    def __init__(self, text, author, publish_date):
        self.text = text
        self.author = author
        self.publish_date = publish_date

    def __str__(self):
        return f'{self.text} / {self.author} / {self.publish_date}'

    def __repr__(self):
        return f'Article(text={self.text}, author={self.author}, publish_data={self.publish_date})'

    def __len__(self):
        return len(self.text)

    def __eq__(self, other):
        return all(
            [
                self.text == other.text,
                self.author == other.author,
                self.publish_date == other.publish_date,
            ]
        )

    def __call__(self, separator='*'):
        print(separator*100)
        print(self.text)
        print(separator*100)
        print(self.publish_date, self.author)
        print(separator * 100)
