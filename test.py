from stackclimber import stackclimber


def test_one():
    # Because this file is called ``test.py`` and not a real module, the
    # logger should be named ``test``.
    assert stackclimber() == 'test'


def test_two():
    test_one()
