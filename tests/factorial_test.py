import pytest
from applications import factorial

def test_fact():
	assert factorial.fact(4)==24