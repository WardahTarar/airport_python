import sys
sys.path.append('./lib/')
from airport import *
from plane import *

def test_checks_for_empty_airport():
  airport = Airport()
  assert airport.hangar == []

def test_lands_plane():
  airport = Airport()
  plane = Plane()
  airport.landing(plane)
  assert airport.hangar == [plane]