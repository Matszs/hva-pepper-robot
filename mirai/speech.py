
class Speech:
	session = tts_service = None

	def __init__(self, session):
		self.session = session
		self.tts_service = self.session.service("ALTextToSpeech")

	def set_language(self, language):
		self.tts_service.setLanguage(language)

	def say(self, text):
		self.tts_service.say(text)
