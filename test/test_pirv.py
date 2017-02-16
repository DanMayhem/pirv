#!python
import pytest
import pirv

def test_instantiate_pirv_election():
  e = pirv.Election(['a','b'])

def test_empty_list_raises_exception():
  with pytest.raises(pirv.EmptyBallotListException):
    e = pirv.Election([])

def test_specify_nonzero_number_of_winners():
  pirv.Election(['a','b','c'],2)

def test_number_of_winners_must_be_less_than_number_of_candidates():
  pirv.Election([1,2,3],2)
  with pytest.raises(pirv.WinnerCountException):
    pirv.Election([1,2,3],3)

def test_zero_winners_fails():
  with pytest.raises(pirv.WinnerCountException):
    pirv.Election([1,2],0)
