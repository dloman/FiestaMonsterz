from Collisions.Collidable import Collidable
from Collisions.ImpactGround import ImpactGround
from Collisions.TypeBasedCollision import TypeBasedCollision
from Death.Killable import Killable
from Drawing.Drawable import Drawable
from Drawing.DrawBlit import DrawBlit
from Events.Event import Event
from Events.JumpEvent import JumpEvent
from Entities.Platform import Platform
from Entities.LoopingFaceRock import LoopingFaceRock
from Movement.Movable import Movable, Movable2D
from Movement.State import State2D
from Utility.Entity import Entity

################################################################################
################################################################################
class JumpMonster(Entity, Movable, Drawable, Event, Killable, Collidable):
  ##############################################################################
  def __init__(self, Window, xPosition, yPosition, InitialVelocity = 20):
    Entity.__init__(self)
    InitialState = \
      State2D( \
        xPosition, \
        yPosition, \
        yAcceleration = 1, \
        Width = 284, \
        Height = 264)
    Movable.__init__(self, Movable2D(InitialState))

    DrawFunctor = DrawBlit(Window, "Images/Monsters/1.png")
    Drawable.__init__(self, DrawFunctor, InitialState)

    JumpFunctor = JumpEvent(InitialState)
    Event.__init__(self, JumpFunctor)

    Killable.__init__(self)

    TypeToActionMap = \
      {Platform : ImpactGround(InitialState, JumpFunctor.ResetJumpCount), \
       LoopingFaceRock : self.Kill}
    CollisionFunctor = \
      TypeBasedCollision(self, TypeToActionMap = TypeToActionMap)
    Collidable.__init__(self, CollisionFunctor, InitialState)

################################################################################
###############################################################################
