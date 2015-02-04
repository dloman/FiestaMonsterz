import pygame

from Games.JumpGame import JumpGame
################################################################################
################################################################################
class MainMenu(object):
  ##############################################################################
  def __init__(self, ScreenShape = (1920, 1080)):
    self.mGameList = [JumpGame]
    self.ScreenShape = ScreenShape

  ##############################################################################
  def GetRandomGame(self):
    self.Window = pygame.display.set_mode(self.ScreenShape)
    pygame.display.set_caption("Window")
    Image = pygame.image.load("Images/Monsters/1.png")

    return JumpGame(self.Window, self.ScreenShape)

################################################################################
################################################################################
