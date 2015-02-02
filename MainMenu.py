import pygame

from Games.JumpGame import JumpGame
################################################################################
################################################################################
class MainMenu(object):
  ##############################################################################
  def __init__(self, ScreenShape = (2200, 1600)):
    self.mGameList = [JumpGame]
    self.ScreenShape = ScreenShape

  ##############################################################################
  def GetRandomGame(self):
    self.Window = pygame.display.set_mode(self.ScreenShape)
    pygame.display.set_caption("Window")

    return JumpGame(self.Window)

################################################################################
################################################################################
