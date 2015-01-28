from Events.Event import Event
from Events.JumpEvent import JumpEvent
from Drawing.Drawable import Drawable
from Drawing.DrawBlit import DrawBlit
from Movement.Movable import Movable, Movable2D
from Movement.State import State2D
from Utility.Entity import Entity

################################################################################
################################################################################
class JumpMonster(Entity, Movable, Drawable, Event):
  ##############################################################################
  def __init__(self, Window, xPosition, yPosition, InitialVelocity = 20):
    Entity.__init__(self)
    InitialState = State2D(xPosition, yPosition)
    Movable.__init__(self, Movable2D(InitialState))

    DrawFunctor = DrawBlit(Window, "Images/Monsters/1.png")
    Drawable.__init__(self, DrawFunctor, InitialState)

    Event.__init__(self, JumpEvent(InitialState))
################################################################################
################################################################################

