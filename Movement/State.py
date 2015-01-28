################################################################################
################################################################################
class State2D(object):
  ##############################################################################
  def __init__(self, \
   xPosition = 0, \
   yPosition = 0, \
   xVelocity = 0, \
   yVelocity = 0, \
   xAcceleration = 0,\
   yAcceleration = 0):
    self.xPosition = xPosition
    self.yPosition = yPosition
    self.xVelocity = xVelocity
    self.yVelocity = yVelocity
    self.xAcceleration = xAcceleration
    self.yAcceleration = yAcceleration

  ##############################################################################
  def GetState(self):
    return \
      self.xPosition, \
      self.yPosition, \
      self.xVelocity, \
      self.yVelocity, \
      self.xAcceleration, \
      self.yAcceleration

  ################################################################################
  def GetPosition(self):
    return self.xPosition, self.yPosition

  ################################################################################
  def GetVelocity(self):
    return self.xVelocity, self.yVelocity

  ################################################################################
  def GetAcceleration(self):
    return self.xAcceleration, yAcceleration

################################################################################
################################################################################


