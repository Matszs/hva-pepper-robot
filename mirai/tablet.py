import time


class Tablet:
	session = tablet_service = None

	def __init__(self, session):
		self.session = session
		self.tablet_service = self.session.service("ALTabletService")

		self.tablet_service.enableWifi()
		self.tablet_service.showWebview("http://198.18.0.1/apps/mirai/video_idle.html")

	def open_page(self, path, delay = 0):
		if delay:
			time.sleep(delay)
		self.tablet_service.showWebview("http://198.18.0.1/apps/mirai/" + path)