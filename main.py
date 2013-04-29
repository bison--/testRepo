#!/usr/bin/env python

# base class
class deathInc(object):

	def __init__(self):
		self._state = None
	
	def printState(self):
		if self._state == None:
			print "dead body class"
		else:
			print self._state
		
	def setState(self, newState):
		if newState == "die":
			self._state = None
		else:
			self._state = newState
		
if __name__ == "__main__":
	di = deathInc()

	di.printState()
	di.setState("reanimated")
	di.printState()
	di.setState("die")
	di.printState()
