# pylint: disable=magic-value-comparison, missing-function-docstring, missing-module-docstring, no-self-use, too-many-public-methods

from dbcreate import hello


def test_hello() -> None:
    assert hello() == 'Hello, world!'


def test_hello_with_author_name() -> None:
    assert hello('Abdulazeez Sherif') \
        == 'Hello, Abdulazeez Sherif!'
