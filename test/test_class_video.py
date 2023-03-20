import pytest

from class_video import Video


def test_str_correct_id():
    video1 = Video('9lO06Zxhu88')
    assert str(video1) == 'Как устроена IT-столица мира / Russian Silicon Valley (English subs)'


def test_str_corrupted_id():
    video1 = Video('broken_video_id')
    assert str(video1) == 'Невозможно получить данные по этому IDшнику'
    assert video1.title is None
    assert video1.like_count is None