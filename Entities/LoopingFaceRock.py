from functools import partial

from Collisions.Collidable import Collidable
from Collisions.TypeBasedCollision import TypeBasedCollision
from Drawing.Drawable import Drawable
from Drawing.DrawBlit import DrawBlit
from Entities.Wall import Wall
from Utility.Entity import Entity
from Death.Killable import Killable
from Death.ResetEntity import ResetEntity
from Movement.Movable import Movable, Movable2D
from Movement.State import State2D
from World import *

################################################################################
################################################################################
class LoopingFaceRock(Entity, Movable, Drawable, Collidable, Killable):
  ##############################################################################
  def __init__(self, World, Window, xPosition, yPosition, xVelocity):
    Entity.__init__(self)
    InitialState = \
      State2D(xPosition, yPosition, xVelocity, Width = 64, Height = 64)
    MoveFunctor = Movable2D(InitialState)
    Movable.__init__(self, MoveFunctor)

    DrawFunctor = DrawBlit(Window, "Images/Items/64-64_EnemyBlockIron.png")
    Drawable.__init__(self, DrawFunctor, InitialState)

    ResetFunctor = \
      partial(LoopingFaceRock, World, Window, xPosition, yPosition, xVelocity)
    Killable.__init__(self, ResetEntity(ResetFunctor, World))

    CollisionFuctor = \
      TypeBasedCollision(TypeToActionMap = {Wall : self.Kill})
    Collidable.__init__(self, CollisionFuctor, InitialState)

################################################################################
################################################################################
