class Airport:
  def __init__(self):
    self.hangar = []

  def landing(self,plane):
    self.hangar.append(plane)