from unittest.mock import patch
import pytest
from pytest import fixture
from datetime import date
from journal.article import Article


@fixture
def article_example():
    return Article(
        text='test text',
        author='some author',
        publish_date=date(2011, 2, 2),
    )


class TestArticle:

    def test_str(self):
        article_example = Article(
            text='test text',
            author='some author',
            publish_date=date(2011, 2, 2),
        )
        assert 'test text / some author / 2011-02-02' == str(article_example)

    def test_str_other(self):
        other_article = Article(
            text='test text 1',
            author='some author',
            publish_date=date(2011, 2, 2),
        )
        assert 'test text 1 / some author / 2011-02-02' == str(other_article)

    @pytest.mark.parametrize(
        "text,result",
        [
            (
                    'test text',
                    'test text / some author / 2011-02-02',
            ),
            (
                    'test text 1',
                    'test text 1 / some author / 2011-02-02',
            ),
            (
                    'test text 2',
                    'test text 2 / some author / 2011-02-02',
            ),
        ]
    )
    def test_str_parametrize(self, text, result):
        article = Article(
            text=text,
            author='some author',
            publish_date=date(2011, 2, 2),
        )
        assert result == str(article)

    def test_str(self):
        params = [
            (
                'test text',
                'test text / some author / 2011-02-02',
            ),
            (
                'test text 1',
                'test text 1 / some author / 2011-02-02',
            ),
            (
                'test text 2',
                'test text 2 / some author / 2011-02-02',
            ),
        ]
        for text, result in params:
            article = Article(
                text=text,
                author='some author',
                publish_date=date(2011, 2, 2),
            )
            assert result == str(article)

    def test_len(self, article_example):
        assert 9 == len(article_example)

    def test_eq_is(self, article_example):
        assert article_example is article_example
        assert article_example == article_example

    def test_eq_other(self, article_example):
        other = Article(
            text='test text',
            author='some author',
            publish_date=date(2011, 2, 2),
        )

        assert article_example == other

    def test_eq_diff(self, article_example, other_article):
        assert article_example != other_article

    def test_call(self, article_example):

        # def mock_print(*args, **kwargs):
        #     mock_print.call_count = True

        # def mock_print(*args, **kwargs):
        #     print('Я замоканный print')
        #
        # # tmp_print = print
        # print = mock_print

        with patch('builtins.print') as mock_print:
            result = article_example()

            mock_print.assert_called_with('*'*100)
            assert mock_print.call_count == 5

        # print = tmp_print
        assert result is None


def test_sum():
    assert 1 + 2 == 3
