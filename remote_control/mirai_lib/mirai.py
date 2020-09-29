#from naoqi import ALProxy
import qi
import sys
import time
from speech import Speech
from motion import Motion
from tablet import Tablet
from face_detection import FaceDetection
from waving_detection import WavingDetection
from audio_player import AudioPlayer
from speech_recognition import SpeechRecognition
from system import System
from navigation import Navigation

class Mirai:
	ip = port = _motion = _speech = _tablet = _face_detection = _wave_detection = _audio_player = _speech_recognition = _navigation = _system = session = None

	def load_modules(self, wait_on_touch = False):
		print("Module :: Load System")
		self._system = System(self.session)

		if wait_on_touch:
			self._system.wait_on_touch()

		print("Module :: Load Speech")
		self._speech = Speech(self.session)
		print("Module :: Load Motion")
		self._motion = Motion(self.session)
		print("Module :: Load Tablet")
		self._tablet = Tablet(self.session)
		print("Module :: Load FaceDetection")
		self._face_detection = FaceDetection(self.session, self)
		print("Module :: Load WavingDetection")
		self._wave_detection = WavingDetection(self.session)
		print("Module :: Load AudioPlayer")
		self._audio_player = AudioPlayer(self.session)
		print("Module :: Load SpeechRecognition")
		self._speech_recognition = SpeechRecognition(self.session)
		print("Module :: Load Navigation")
		self._navigation = Navigation(self.session)

	def __init__(self, ip, port = 9559):
		self.ip = ip
		self.port = port

	def start(self, wait_on_touch = False):
		self.connect(wait_on_touch)
		#self.load_modules(wait_on_boot)
		self.motion().stand()

	def connect(self, wait_on_touch = False):
		self.session = qi.Session()

		try:
			self.session.connect("tcp://" + self.ip + ":" + str(self.port))
			self.load_modules(wait_on_touch)
		except RuntimeError:
			print ("Can't connect to Naoqi at ip \"" + self.ip + "\" on port " + str(self.port))
			self.checkConnection()

	def checkConnection(self):
		connected = self.session.isConnected()

		print("Connection status: " + str(connected))

		if not connected:
			time.sleep(.1)
			print("Trying to reconnect...")
			self.connect()

	def speech(self):
		self.checkConnection()
		return self._speech

	def motion(self):
		self.checkConnection()
		return self._motion

	def tablet(self):
		self.checkConnection()
		return self._tablet

	def face_detection(self):
		self.checkConnection()
		return self._face_detection

	def wave_detection(self):
		self.checkConnection()
		return self._wave_detection

	def audio_player(self):
		self.checkConnection()
		return self._audio_player

	def speech_recognition(self):
		self.checkConnection()
		return self._speech_recognition

	def navigation(self):
		self.checkConnection()
		return self._navigation

	def system(self):
		self.checkConnection()
		return self._system

	def sleep(self):
		return self._motion.sleep()

	def wake_up(self):
		return self._motion.wake_up()

	def register_service(self, name, instance):
		try:
			self.session.registerService(name, instance)
		except:
			print("Servive already registered.")
		return self


#from naoqi import ALProxy
#tts = ALProxy("ALTextToSpeech", "145.28.47.180", 9559)
#motion = ALProxy("ALMotion", "145.28.47.180", 9559)
#motion.setStiffnesses("Body", 1.0)
#tts.setLanguage("Dutch")
#tts.say("Hallo wereld!")
