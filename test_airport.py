import sys
sys.path.append('./lib/')
from airport import *


def test_checks_for_empty_airport():
  airport = Airport()
  assert airport.runway == []