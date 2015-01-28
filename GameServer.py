#!/usr/bin/python
import sys
from twisted.internet import reactor, protocol
from twisted.internet.task import LoopingCall
from socket import *
#from MonsterParty import MonsterParty

################################################################################
################################################################################
class Echo(protocol.Protocol):
    """This is just about the simplest possible protocol"""

    def dataReceived(self, data):
      print 'data = ', data

################################################################################
################################################################################
class Game():

  def __init__(self):
    self.mCounter = 0

  def Update(self):
    self.mCounter += 1
    if self.mCounter > 100000:
      print 'Doing game stuff'
      self.mCounter = 0

################################################################################
################################################################################
if __name__ == '__main__':
  MainGame = Game()
  GameLoopingCall = LoopingCall(MainGame.Update)
  GameLoopingCall.start(1/60) #60 fps

  factory = protocol.ServerFactory()
  factory.protocol = Echo
  reactor.listenTCP(42069, factory)
  reactor.run()
