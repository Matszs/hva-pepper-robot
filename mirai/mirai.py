#from naoqi import ALProxy
import qi
import sys
from speech import Speech
from motion import Motion

class Mirai:
	ip = port = _motion = _speech = session = None

	def load_modules(self):
		self._speech = Speech(self.session)
		self._motion = Motion(self.session)

	def __init__(self, ip, port = 9559):
		self.ip = ip
		self.port = port

		self.session = qi.Session()

		try:
			self.session.connect("tcp://" + self.ip + ":" + str(self.port))
		except RuntimeError:
			print ("Can't connect to Naoqi at ip \"" + self.ip + "\" on port " + str(self.port))
			sys.exit(1)

		self.load_modules()

	def speech(self):
		return self._speech

	def motion(self):
		return self._motion



#from naoqi import ALProxy
#tts = ALProxy("ALTextToSpeech", "145.28.47.180", 9559)
#motion = ALProxy("ALMotion", "145.28.47.180", 9559)
#motion.setStiffnesses("Body", 1.0)
#tts.setLanguage("Dutch")
#tts.say("Hallo wereld!")
