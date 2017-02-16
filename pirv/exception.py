#!python

class EmptyBallotListException(ValueError):
  """The provided list of candidates for the election is empty"""

class WinnerCountException(ValueError):
  """The provided winner count is greater than the number of candidates or less than 1"""
