from Drawing.Drawable import Drawable
from Drawing.DrawPlatform import DrawPlatform
from Movement.Movable import Movable, Movable2D
from Movement.State import State2D
from Utility.Entity import Entity

################################################################################
################################################################################
class Platform(Entity, Movable, Drawable):
  ##############################################################################
  def __init__(self, Window, xPosition, yPosition, TileType, Length = 1):
    Entity.__init__(self)
    InitialState = State2D(xPosition, yPosition)
    Movable.__init__(self, Movable2D(InitialState))

    DrawFunctor = \
      DrawPlatform(Window, "Images/platformPack/PNG/Tiles/" + TileType, Length)

    Drawable.__init__(self, DrawFunctor, InitialState)
################################################################################
################################################################################

