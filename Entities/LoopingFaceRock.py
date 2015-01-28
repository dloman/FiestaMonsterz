from functools import partial

from Collisions.Collidable import Collidable
from Collisions.ResetEntity import ResetEntity
from Drawing.Drawable import Drawable
from Drawing.DrawBlit import DrawBlit
from Utility.Entity import Entity
from Death.Killable import Killable
from Movement.Movable import Movable, Movable2D
from Movement.State import State2D
from World import *

################################################################################
################################################################################
class LoopingFaceRock(Entity, Movable, Drawable, Collidable, Killable):
  ##############################################################################
  def __init__(self, World, Window, xPosition, yPosition, xVelocity):
    Entity.__init__(self)
    InitialState = State2D(xPosition, yPosition, xVelocity)
    MoveFunctor = Movable2D(InitialState)
    Movable.__init__(self, MoveFunctor)

    DrawFunctor = DrawBlit(Window, "Images/Items/64-64_EnemyBlockIron.png")
    Drawable.__init__(self, DrawFunctor, InitialState)

    Killable.__init__(self, lambda x: True) #Dies on collisions w/ all objects

    ResetFunctor = \
      partial(LoopingFaceRock, World, Window, xPosition, yPosition, xVelocity)
    CollisionFuctor = ResetEntity(ResetFunctor, self, World)
    Collidable.__init__(self, CollisionFuctor, InitialState)

################################################################################
################################################################################
