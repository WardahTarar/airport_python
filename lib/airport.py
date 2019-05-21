class Airport:
  def __init__(self):
    self.hangar = []

  def land(self,plane):
    self.hangar.append(plane)

  def takeoff(self,plane):
    self.hangar.pop(-1)