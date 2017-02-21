#!python

import math

from .exception import EmptyBallotListException, InvalidBallotException, NoVotesException

class Election():
  def __init__(self, candidates):
    if len(candidates) < 2:
      raise EmptyBallotListException()
    self._candidates = candidates
    self._votes = []

  def vote(self, ballot):
    for c in ballot:
      if c not in self._candidates:
        raise InvalidBallotException
    if len(ballot) > 0:
      self._votes.append(ballot)

  def get_vote_count(self):
    return len(self._votes)

  def votes_required_to_win(self):
    if len(self._votes) == 0:
      raise NoVotesException
    return math.ceil(len(self._votes)/2.+.5)

  def winner(self):
    tally = self._tally_votes()
    (first, last) = self._find_results(tally)
    if tally[first[0]] >= self.votes_required_to_win():
      return first[0]
    e = Election([x for x in self._candidates if x not in last])
    for v in self._votes:
      e.vote([x for x in v if x not in last])
    return e.winner()

  def _tally_votes(self):
    tally = {}
    for c in self._candidates:
      tally[c]=0
    for v in self._votes:
      tally[v[0]]+=1
    return tally

  def _find_results(self, tally):
    first = None
    last = None
    for c in tally:
      if first is None:
        first = [c]
      elif tally[c] == tally[first[0]]:
        first.append(c)
      elif tally[c] > tally[first[0]]:
        first = [c]
      if last is None:
        last = [c]
      elif tally[c] == tally[last[0]]:
        last.append(c)
      elif tally[c] < tally[last[0]]:
        last = [c]
    return (first, last)
