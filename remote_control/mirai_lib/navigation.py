
class Navigation:
	session = navigation_service = None

	def __init__(self, session):
		self.session = session
		self.navigation_service = self.session.service("ALNavigation")

	def forward(self):
		print(self.navigation_service.moveAlong(["Composed", ["Holonomic", ["Line", [1.0, 0.0]], 0.0, 5.0], ["Holonomic", ["Line", [-1.0, 0.0]], 0.0, 10.0]]))
		return self
