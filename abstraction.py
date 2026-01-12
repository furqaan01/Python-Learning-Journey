class car:
  def __init__(self):
    self.acceleration=False
    self.clutch=False
    self.brake=True
  def start(self):
    self.acceleration=True
    self.clutch=True
    self.brake=False 
    print("Car Started") 
a=car()
a.start()     

#it basically hides the implementation of the car whn it needs to bestarted but only provides the essential data