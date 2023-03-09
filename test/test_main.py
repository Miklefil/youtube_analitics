import pytest

from main import Channel


@pytest.fixture
def coll():
    channel = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
    return channel

@pytest.fixture
def coll2():
    channel = Channel('UC1eFXmJNkjITxPFWTy6RsWg')
    return channel


def test_str(coll):
    assert str(coll) == 'Youtube-канал: вДудь'


def test_add(coll, coll2):
    assert coll + coll2 == 14000000


def test_lt(coll, coll2):
    assert coll.__lt__(coll2) is False


def test_gt(coll, coll2):
    assert coll.__gt__(coll2) is True