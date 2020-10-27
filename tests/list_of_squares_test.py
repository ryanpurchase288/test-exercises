import pytest
from applications import list_of_squares

def test_square():
	assert list_of_squares.list_of_squares(4)=={1: 1, 2: 4, 3: 9, 4: 16}