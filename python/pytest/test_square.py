import pytest
import math


@pytest.mark.square
def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5
