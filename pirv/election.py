#!python

from .exception import EmptyBallotListException, WinnerCountException

class Election():
  def __init__(self, candidates, winner_count=1):
    if len(candidates) < 2:
      raise EmptyBallotListException()
    if len(candidates) <= winner_count:
      raise WinnerCountException()
    if winner_count < 1:
      raise WinnerCountException()
