################################################################################
################################################################################
class Movable(object):
  ##############################################################################
  def __init__(self, MoveFunctor):
    self.MoveFunctor = MoveFunctor

  ##############################################################################
  @property
  def MoveFunctor(self):
    return self.__MoveFunctor

  ##############################################################################
  @MoveFunctor.setter
  def MoveFunctor(self, MoveFunctor):
    if not callable(MoveFunctor):
      raise TypeError(str(type(MoveFunctor)) + ' must be callable')
    self.__MoveFunctor = MoveFunctor

  ##############################################################################
  def Move(self):
    self.__MoveFunctor()

################################################################################
################################################################################
class Movable2D(object):
  ##############################################################################
  def __init__(self, InitialState):
    self.State = InitialState

  ##############################################################################
  def __call__(self):
    self.State.Rectangle.move_ip(self.State.xVelocity, self.State.yVelocity)

    self.State.xVelocity += self.State.xAcceleration
    self.State.yVelocity += self.State.yAcceleration

  ################################################################################
  def GetPosition(self):
    return self.State.GetPosition()

################################################################################
################################################################################
