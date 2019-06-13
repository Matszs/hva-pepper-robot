
class Tablet:
	session = tablet_service = None

	def __init__(self, session):
		self.session = session
		self.tablet_service = self.session.service("ALTabletService")

		self.tablet_service.enableWifi()
		self.tablet_service.showWebview("http://198.18.0.1/apps/mirai")
