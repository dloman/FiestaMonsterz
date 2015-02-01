#!/usr/bin/python

from sys import argv
from socket import *

################################################################################
def SendBroadcast(ScreenId):
  print "Sending Broadcast Screen Id =", ScreenId
  broadcast = socket(AF_INET, SOCK_DGRAM)
  broadcast.bind(('', 0))
  broadcast.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
  broadcast.sendto(ScreenId, ('<broadcast>', 31337))

################################################################################
################################################################################
if __name__ == '__main__':
  if len(argv) > 1:
    if argv[1] == "2":
      SendBroadcast("TwoButton")
      exit()
    elif argv[1] == '-h':
      print 'Usage: SendBroadcast ScreenId'
      exit()
  SendBroadcast("OneButton")

