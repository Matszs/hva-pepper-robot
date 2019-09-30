
class System:
	session = system_service = None

	def __init__(self, session):
		self.session = session
		self.system_service = self.session.service("ALSystem")

	def reboot(self):
		self.system_service.reboot()
		return self

	def shutdown(self):
		self.system_service.shutdown()
		return self