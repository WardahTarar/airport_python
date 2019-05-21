from plane import *

def test_create_instance_of_plane():
  plane = Plane()
  if isinstance(plane,Plane):
    print(" I have a plane")