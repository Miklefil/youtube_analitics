import pytest

from class_plvideo import PLVideo


def test_str():
    video2 = PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')
    assert str(video2) == 'Пушкин: наше все? (Литература)'