#!/usr/bin/env python

# base class
class deathInc(object):
	def printState(self):
		print "dead body class"
		
	def setState(self, newState):
		self._state = newState
		

di = deathInc()

di.printState()
di.setState("reanimated")
di.printState()
