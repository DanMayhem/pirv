#!python
#IRV examples from the wikipedia article.
#https://en.wikipedia.org/wiki/Instant-runoff_voting

import pirv

def test_wiki_five_voters_three_candidates():
  e = pirv.Election(['Bob','Sue','Bill'])
  e.vote(['Bob','Bill','Sue'])
  e.vote(['Sue','Bob','Bill'])
  e.vote(['Bill','Sue','Bob'])
  e.vote(['Bob','Bill','Sue'])
  e.vote(['Sue','Bob','Bill'])
  assert e.winner() == 'Sue'

def test_wiki_Tennessee_capital_election():
  e = pirv.Election(['Memphis','Knoxville','Nashville','Chattanooga'])
  for i in range(42):
    e.vote(['Memphis','Nashville','Chattanooga','Knoxville'])
  for i in range(26):
    e.vote(['Nashville','Chattanooga','Knoxville','Memphis'])
  for i in range(15):
    e.vote(['Chattanooga','Knoxville','Nashville','Memphis'])
  for i in range(17):
    e.vote(['Knoxville','Chattanooga','Nashville','Memphis'])
  assert e.winner() == 'Knoxville'
