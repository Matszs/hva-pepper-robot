import time
import math

class Motion:
	session = motion_service = posture_service = None

	def __init__(self, session):
		self.session = session
		self.motion_service = self.session.service("ALMotion")
		self.posture_service = self.session.service("ALRobotPosture")

		#self.stand() # default standing

	def stand(self):
		self.posture_service.goToPosture("StandInit", 0.1)

	def sleep(self):
		self.motion_service.rest()

	def wake_up(self):
		self.motion_service.wakeUp()

	def set_head(self, x, y, speed = 0.1):
		self.motion_service.setStiffnesses("Head", 1.0)

		self.motion_service.setAngles("HeadYaw", x, speed)
		self.motion_service.setAngles("HeadPitch", y, speed)

	def move(self):
		print("move")
