################################################################################
################################################################################
class JumpEvent(object):
  ##############################################################################
  def __init__(self, State, InitialVelocity = -20, MaxNumberOfJumps = 2):
    self.State = State
    self.InitialVelocity = InitialVelocity
    self.MaxNumberOfJumps = MaxNumberOfJumps
    self.NumberOfJumps = 0

  ##############################################################################
  def ProcessEvent(self, Event):
    if self.NumberOfJumps < self.MaxNumberOfJumps:
      self.State.yVelocity = self.InitialVelocity
      self.NumberOfJumps += 1

  ##############################################################################
  def ResetJumpCount(self):
    self.NumberOfJumps = 0

################################################################################
################################################################################
