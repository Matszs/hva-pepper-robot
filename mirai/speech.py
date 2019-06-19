DEFAULT_PITCH = 1.2

class Speech:
	session = tts_service = animated_speech_service = speak_move_service = None

	def __init__(self, session):
		self.session = session
		self.tts_service = self.session.service("ALTextToSpeech")
		self.animated_speech_service = self.session.service("ALAnimatedSpeech")
		self.speak_move_service = self.session.service("ALSpeakingMovement")
		self.set_default_pitch()

		self.speak_move_service.setEnabled(True)

	# Speed - from 50 (slow) to 400 (fast)
	def set_speed(self, speed):
		self.tts_service.setParameter("speed", speed)
		return self

	def set_volume(self, volume):
		self.tts_service.setVolume(volume)
		return self

	def set_language(self, language):
		self.tts_service.setLanguage(language)
		return self

	def set_pitch(self, pitch):
		self.tts_service.setParameter("pitchShift", pitch)
		return self

	def set_default_pitch(self):
		self.tts_service.setParameter("pitchShift", DEFAULT_PITCH)
		return self

	def say(self, text):
		self.tts_service.say(text)
		return self

	# http://doc.aldebaran.com/2-5/naoqi/audio/alanimatedspeech.html
	def asay(self, text):
		self.animated_speech_service.say(text)
		return self

	def enable_auto_movement(self):
		self.speak_move_service.setEnabled(True)
		return self

	def disable_auto_movement(self):
		self.speak_move_service.setEnabled(False)
		return self