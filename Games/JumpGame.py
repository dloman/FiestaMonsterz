import pygame
from random import randint

from Entities.LoopingFaceRock import LoopingFaceRock
from Entities.JumpMonster import JumpMonster
from Entities.Platform import Platform
from Entities.Wall import Wall
from Utility.AdaptiveScreenSize import AdaptiveScreenSize
from World import World

gBlack = (0,0,0)
################################################################################
################################################################################
class JumpGame():
  ##############################################################################
  def __init__(self, Window, ScreenShape):
    self.Window = Window
    self.AdaptiveScreenSize = AdaptiveScreenSize(ScreenShape)
    self.MainWorld = World(Window.get_size())

    xPosition, yPosition, Length,Height = \
      self.AdaptiveScreenSize.GetPositionWidthAndHeight(0, 0, 0, 100)
    self.MainWorld.AddEntity(Wall(xPosition, yPosition, Length, Height))

    xPosition, yPosition, Length,Height = \
      self.AdaptiveScreenSize.GetPositionWidthAndHeight(1, 100, 1000, 0)
    self.MainWorld.AddEntity(Wall(xPosition, yPosition, Length, Height))

    xPosition, yPosition = self.AdaptiveScreenSize.GetPosition(100, 59)
    self.MainWorld.AddEntity(\
      LoopingFaceRock(self.MainWorld, self.Window, xPosition, yPosition, -15))

    xPosition, yPosition = self.AdaptiveScreenSize.GetPosition(50, 65)
    self.MainWorld.AddEntity(\
      Platform(self.Window, xPosition, yPosition, 'ZigzagGrass_', 26))

  ##############################################################################
  def AddMonster(self, Id):
    xPosition, yPosition = self.AdaptiveScreenSize.GetPosition(50, 25)
    self.MainWorld.AddEntity(JumpMonster(self.Window, xPosition, yPosition), Id)

  ##############################################################################
  def Update(self):
    self.Window.fill(gBlack)
    self.MainWorld.Update()
    pygame.display.flip()

  ##############################################################################
  def AddEvent(self, Id, Event):
    self.MainWorld.AddEventToQueue(Id, Event)

################################################################################
################################################################################
