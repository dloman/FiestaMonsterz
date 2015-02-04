################################################################################
################################################################################
class AdaptiveScreenSize():
  ##############################################################################
  def __init__(self, ScreenShape):
    self.Width = ScreenShape[0]
    self.Height = ScreenShape[1]

  ##############################################################################
  def GetPosition(self, X, Y):
    return (self.Width * X / 100.), (self.Height * Y / 100)

  ##############################################################################
  def GetPositionWidthAndHeight(self, X, Y, Width, Height):
    return \
      (self.Width * X / 100.), \
      (self.Height * Y / 100), \
      (self.Width * Width/100), \
      (self.Height * Height/100)
