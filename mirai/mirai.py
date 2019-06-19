#from naoqi import ALProxy
import qi
import sys
from speech import Speech
from motion import Motion
from tablet import Tablet
from face_detection import FaceDetection
from waving_detection import WavingDetection
from audio_player import AudioPlayer
from speech_recognition import SpeechRecognition

class Mirai:
	ip = port = _motion = _speech = _tablet = _face_detection = _wave_detection = _audio_player = _speech_recognition = session = None

	def load_modules(self):
		self._speech = Speech(self.session)
		self._motion = Motion(self.session)
		self._tablet = Tablet(self.session)
		self._face_detection = FaceDetection(self.session)
		self._wave_detection = WavingDetection(self.session)
		self._audio_player = AudioPlayer(self.session)
		self._speech_recognition = SpeechRecognition(self.session)

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

	def tablet(self):
		return self._tablet

	def face_detection(self):
		return self._face_detection

	def wave_detection(self):
		return self._wave_detection

	def audio_player(self):
		return self._audio_player

	def speech_recognition(self):
		return self._speech_recognition

	def sleep(self):
		return self._motion.sleep()

	def wake_up(self):
		return self._motion.wake_up()



#from naoqi import ALProxy
#tts = ALProxy("ALTextToSpeech", "145.28.47.180", 9559)
#motion = ALProxy("ALMotion", "145.28.47.180", 9559)
#motion.setStiffnesses("Body", 1.0)
#tts.setLanguage("Dutch")
#tts.say("Hallo wereld!")
