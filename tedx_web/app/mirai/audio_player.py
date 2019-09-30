import time


class AudioPlayer:
	session = audio_player_service = None

	def __init__(self, session):
		self.session = session
		self.audio_player_service = self.session.service("ALAudioPlayer")

	def play_song(self, file_name, asynchrone = True):
		fileId = self.audio_player_service.loadFile("/opt/aldebaran/var/www/apps/mirai/assets/sounds/" + file_name)
		self.audio_player_service.play(fileId, _async=asynchrone)
		#currentPos = self.audio_player_service.getCurrentPosition(fileId)

		return self