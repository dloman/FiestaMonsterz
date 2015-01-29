import pygame
################################################################################
################################################################################
class DrawPlatform(object):
  ##############################################################################
  def __init__(self, Window, TileFileNamePrefix, PlatformLength, TileSize = 32):
    self.Window = Window
    self.__PlatformLength = PlatformLength
    self.__TileSize = TileSize

    self.__LeftBlock = pygame.image.load(TileFileNamePrefix + '2RoundLeft.png')
    self.__RightBlock = \
      pygame.image.load(TileFileNamePrefix + '2RoundRight.png')

    self.__MiddleBlock = pygame.image.load(TileFileNamePrefix + 'Square.png')
    self.__SingleBlock = pygame.image.load(TileFileNamePrefix + 'Round.png')

  ##############################################################################
  def __call__(self, Position):
    xPosition, yPosition = Position
    xPosition -= self.__TileSize
    if self.__PlatformLength == 1:
      self.Window.blit(self.__SingleBlock, (xPosition, yPosition))
    else:
      Offset = 0
      if self.__PlatformLength % 2:
        self.Window.blit(self.__MiddleBlock, (xPosition, yPosition))
        Offset += self.__TileSize

      for i in range(self.__PlatformLength - 3):
        Offset += self.__TileSize
        self.Window.blit(self.__MiddleBlock, (xPosition + Offset, yPosition))
        self.Window.blit(self.__MiddleBlock, (xPosition - Offset, yPosition))
      Offset += self.__TileSize
      self.Window.blit(self.__RightBlock, (xPosition + Offset, yPosition))
      self.Window.blit(self.__LeftBlock, (xPosition - Offset, yPosition))

################################################################################
################################################################################

