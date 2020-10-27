import pytest
from applications import factorial

def test_fact():
	assert factorial.fact(4)==24

def test_fact_1():
	assert factorial.fact(7)==5040

def test_fact_2():
	assert factorial.fact(25)==15511210043330985984000000

        