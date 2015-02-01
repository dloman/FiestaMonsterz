from Collisions.Collidable import Collidable
from Collisions.FallingDeath import FallingDeath
from Collisions.ImpactGround import ImpactGround
from Collisions.TypeBasedCollision import TypeBasedCollision
from Death.Killable import Killable
from Drawing.Drawable import Drawable
from Drawing.DrawBlit import DrawBlit
from Events.Event import Event
from Events.JumpEvent import JumpEvent
from Entities.Platform import Platform
from Entities.LoopingFaceRock import LoopingFaceRock
from Entities.Wall import Wall
from Movement.Movable import Movable, Movable2D
from Movement.State import State2D
from Utility.Entity import Entity

################################################################################
################################################################################
class JumpMonster(Entity, Movable, Drawable, Event, Killable, Collidable):
  ##############################################################################
  def __init__(self, Window, xPosition, yPosition, JumpVelocity = -20):
    Entity.__init__(self)
    InitialState = \
      State2D( \
        xPosition, \
        yPosition, \
        yAcceleration = 1, \
        Width = 224, \
        Height = 264)
    Movable.__init__(self, Movable2D(InitialState))

    DrawFunctor = DrawBlit(Window, "Images/Monsters/1.png")
    Drawable.__init__(self, DrawFunctor, InitialState)

    JumpFunctor = JumpEvent(InitialState, JumpVelocity)
    Event.__init__(self, JumpFunctor)


    DeathFunctor = FallingDeath(self, Window, "Images/Monsters/Dead1.png")
    Killable.__init__(self)

    TypeToActionMap = \
      {Platform : ImpactGround(JumpFunctor.ResetJumpCount), \
       LoopingFaceRock : DeathFunctor, \
       Wall : self.Kill}
    CollisionFunctor = TypeBasedCollision(TypeToActionMap = TypeToActionMap)
    Collidable.__init__(self, CollisionFunctor, InitialState)

################################################################################
###############################################################################
