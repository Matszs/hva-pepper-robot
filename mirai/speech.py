
class Speech:
	session = tts_service = None

	def __init__(self, session):
		self.session = session
		self.tts_service = self.session.service("ALTextToSpeech")

		# Set pitch of the voice
		self.tts_service.setParameter("pitchShift", 1.2)

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

	def say(self, text):
		self.tts_service.say(text)
		return self
