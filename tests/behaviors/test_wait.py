from datetime import timedelta

from mountequist import behaviors


def test_wait_properly_converts():
    behavior = behaviors.Wait(timedelta(seconds=60))
    assert behavior._convert_timedelta() == 60000


def test_wait_as_dict():
    result = behaviors.Wait(timedelta(seconds=60)).as_dict()
    assert "wait" in result
    assert result["wait"] == 60000
