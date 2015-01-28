from Utility.Utility import DoesntHaveMethod
################################################################################
################################################################################
class Drawable(object):
  ##############################################################################
  def __init__(self, DrawFunctor, GetPositionFunctor):
    self.DrawFunctor = DrawFunctor
    self.GetPositionFunctor = GetPositionFunctor

  ##############################################################################
  @property
  def DrawFunctor(self):
    return self.__DrawFunctor

  ##############################################################################
  @DrawFunctor.setter
  def DrawFunctor(self, DrawFunctor):
    if not callable(DrawFunctor):
      raise TypeError(str(type(DrawFunctor)) + " must be a callable type")
    self.__DrawFunctor = DrawFunctor

  ##############################################################################
  @property
  def GetPositionFunctor(self):
    return self.__GetPositionFunctor

  ##############################################################################
  @GetPositionFunctor.setter
  def GetPositionFunctor(self, GetPositionFunctor):
    if DoesntHaveMethod(GetPositionFunctor, 'GetPosition'):
      raise TypeError(str(type(GetPositionFunctor)) + 'must be callable')
    self.__GetPositionFunctor = GetPositionFunctor

  ##############################################################################
  def Draw(self):
    self.__DrawFunctor(self.GetPosition())

  ##############################################################################
  def GetPosition(self):
    return self.GetPositionFunctor.GetPosition()

################################################################################
################################################################################
