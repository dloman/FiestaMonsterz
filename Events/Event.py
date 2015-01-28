import Queue

from Utility.Utility import DoesntHaveMethod
################################################################################
################################################################################
class Event(object):
  ##############################################################################
  def __init__(self, EventFunctor):
    self.EventFunctor = EventFunctor
    self.__EventQueue = Queue.Queue()

  ##############################################################################
  @property
  def EventFunctor(self):
    return self.__EventFunctor

  ##############################################################################
  @EventFunctor.setter
  def EventFunctor(self, EventFunctor):
    if DoesntHaveMethod(EventFunctor, 'ProcessEvent'):
      raise TypeError(str(type(EventFunctor)) + ' must define ProcessEvent')
    self.__EventFunctor = EventFunctor

  ##############################################################################
  def AddEventToQueue(self, Event):
    self.__EventQueue.put(Event)

  ##############################################################################
  def ProcessEvents(self):
    while not self.__EventQueue.empty():
      self.__EventFunctor.ProcessEvent(self.__EventQueue.get())

################################################################################
################################################################################
