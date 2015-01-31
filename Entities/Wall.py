from Collisions.Collidable import Collidable
from Movement.Movable import Movable, Movable2D
from Movement.State import State2D
from Utility.Entity import Entity
################################################################################
################################################################################
class Wall(Entity, Movable, Collidable):
  ##############################################################################
  def __init__(self, xPosition, yPosition, Width = 1, Height = 1):
    Entity.__init__(self)
    InitialState = State2D(xPosition, yPosition, Width = Width, Height = Height)
    Movable.__init__(self, Movable2D(InitialState))

    Collidable.__init__(self, lambda x,y: None, InitialState)

################################################################################
################################################################################
