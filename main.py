
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
		self._state = newState
		

di = deathInc()

di.printState()
di.setState("reanimated")
di.printState()
