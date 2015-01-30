################################################################################
################################################################################
class ImpactGround(object):
  ##############################################################################
  def __init__(self, InitialState):
    self.State = InitialState

  ###############################################################################
  @property
  def State(self):
    return self.__State

  ###############################################################################
  @State.setter
  def State(self, State):
    if not hasattr(State, 'yVelocity'):
      raise TypeError(str(type(State)) + 'must have yVelocity value')
    self.__State = State

  ###############################################################################
  def __call__(self, Rectangle):
    self.State.yVelocity = 0
    self.State.Rectangle.y = Rectangle.y - self.State.Rectangle.height

################################################################################
################################################################################


