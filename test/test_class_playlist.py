import pytest
from datetime import datetime, timedelta

from class_playlist import PlayList


@pytest.fixture
def coll():
    pl = PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')
    return pl

def test_init(coll):
    assert coll.title == 'Редакция. АнтиТревел'
    assert coll.url == 'https://www.youtube.com/playlist?list=PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb'


def test_total_duration(coll):
    assert coll.total_duration == timedelta(seconds=13261)

def test_most_popular_video(coll):
    assert coll.most_popular_video() == 'https://www.youtube.com/watch?v=9Bv2zltQKQA'