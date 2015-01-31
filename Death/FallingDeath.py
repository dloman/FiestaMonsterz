from Collisions.TypeBasedCollision import TypeBasedCollision
from Drawing.DrawBlit import DrawBlit
from Entities.Wall import Wall
################################################################################
################################################################################
class FallingDeath(object):
  ##############################################################################
  def __init__(self, DyingObject, Window, DeadImageFileName):
    self.Window = Window
    self.DyingObject = DyingObject
    self.DeadImageFileName = DeadImageFileName

  ##############################################################################
  def __call__(self, CollidedObject, State):
    State.xVelocity -= 3
    self.DyingObject.DrawFunctor = DrawBlit(self.Window, self.DeadImageFileName)
    self.DyingObject.CollisionFunctor = \
      TypeBasedCollision(TypeToActionMap = {Wall : self.DyingObject.Kill})




