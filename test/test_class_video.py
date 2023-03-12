import pytest

from class_video import Video


def test_str():
    video1 = Video('9lO06Zxhu88')
    assert str(video1) == 'Как устроена IT-столица мира / Russian Silicon Valley (English subs)'