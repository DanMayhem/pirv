#!python
import pytest
import pirv

def _ab_election():
    return pirv.Election(['a','b'])

def test_instantiate_pirv_election():
  _ab_election()

def test_empty_list_raises_exception():
  with pytest.raises(pirv.EmptyBallotListException):
    e = pirv.Election([])

def test_submit_ballot():
    e = _ab_election()
    e.vote(['a','b'])

def test_get_vote_count():
    e = _ab_election()
    assert e.get_vote_count() == 0

def test_submit_write_in_ballot():
    with pytest.raises(pirv.InvalidBallotException):
        _ab_election().vote(['c'])

def test_accept_empty_ballot():
  _ab_election().vote([])

def test_verify_vote_counts():
  e = _ab_election()
  assert e.get_vote_count() == 0
  e.vote(['a','b'])
  assert e.get_vote_count() == 1
  e.vote(['a'])
  assert e.get_vote_count() == 2

def test_some_votes_required_to_win():
  with pytest.raises(pirv.NoVotesException):
    _ab_election().votes_required_to_win()

def test_verify_votes_required_to_win():
  e = _ab_election()
  e.vote(['a'])
  assert e.votes_required_to_win() == 1
  e.vote(['a'])
  assert e.votes_required_to_win() == 2
  e.vote(['a'])
  e.vote(['a'])
  e.vote(['a'])
  assert e.votes_required_to_win() == 3

def test_verify_runoff_scenario_1():
  e = _ab_election()
  e.vote(['a','b'])
  e.vote(['a'])
  assert e.winner() == 'a'

def test_verify_runoff_scenario_2():
  e = pirv.Election([1,2,3])
  e.vote([1,3])
  e.vote([2,3])
  e.vote([1,3])
  assert e.winner() == 1

def test_verify_runoff_scenario_3():
  e = pirv.Election([1,2,3,4])
  e.vote([1,3])
  e.vote([2,3])
  e.vote([1,3])
  e.vote([3])
  assert e.winner() == 1

def test_verify_runoff_scenario_4():
  e =pirv.Election([1,2,3,4])
  e.vote([1,4])
  e.vote([2,4])
  e.vote([2,4])
  e.vote([4,2])
  e.vote([4,3])
  e.vote([3,4])
  assert e.votes_required_to_win() == 4
  t = e._tally_votes()
  assert t[1] == 1
  assert t[2] == 2
  assert t[3] == 1
  assert t[4] == 2
  (winners, losers) = e._find_results(t)
  assert 1 in losers
  assert 3 in losers
  assert 2 in winners
  assert 4 in winners
  assert e.winner() == 4
