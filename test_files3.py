import pytest


@pytest.mark.sample
def test_data1():
    a = 1
    b = 1
    assert a == b
@pytest.mark.sample
def test_data2():
    a = "mukunth"
    b = "MUKUNTH"
    assert a == b.lower()

