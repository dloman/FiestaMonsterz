import pygame
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
   yAcceleration = 0, \
   Width = 0, \
   Height = 0):
    self.Rectangle = pygame.Rect((xPosition, yPosition), (Width, Height))
    self.xVelocity = xVelocity
    self.yVelocity = yVelocity
    self.xAcceleration = xAcceleration
    self.yAcceleration = yAcceleration

  ##############################################################################
  def GetState(self):
    return \
      self.Rectangle, \
      self.xVelocity, \
      self.yVelocity, \
      self.xAcceleration, \
      self.yAcceleration

  ################################################################################
  def GetRectangle(self):
    return self.Rectangle

  ################################################################################
  def GetPosition(self):
    return self.Rectangle.x, self.Rectangle.y

  ################################################################################
  def GetVelocity(self):
    return self.xVelocity, self.yVelocity

  ################################################################################
  def GetAcceleration(self):
    return self.xAcceleration, yAcceleration

################################################################################
################################################################################


