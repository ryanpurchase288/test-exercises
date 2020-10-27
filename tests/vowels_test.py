import pytest
from applications import vowels

def test_vowel():
	assert vowels.vowels('Ryan')==1

def test_vowel1():
	assert vowels.vowels('Lewis')==2

def test_vowel2():
	assert vowels.vowels('George')==3

def test_vowel3():
	assert vowels.vowels('Purchase')==3        