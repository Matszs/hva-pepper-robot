import time
import math

class Motion:
	session = motion_service = posture_service = animation_service = None

	def __init__(self, session):
		self.session = session
		self.motion_service = self.session.service("ALMotion")
		self.posture_service = self.session.service("ALRobotPosture")
		self.animation_service = self.session.service("ALAnimationPlayer")

		# Disable the autonomous ability of the arms.
		self.motion_service.setIdlePostureEnabled("Arms", False)

		self.stand() # default standing

	def stand(self, speed = 0.1):
		self.posture_service.goToPosture("StandInit", speed)
		self.set_head(0, 0)
		return self

	def sleep(self):
		self.motion_service.rest()
		return self

	def wake_up(self):
		self.motion_service.wakeUp()
		return self

	def set_head(self, x, y, speed = 0.1):
		self.motion_service.setStiffnesses("Head", 1.0)

		self.motion_service.setAngles("HeadYaw", x, speed)
		self.motion_service.setAngles("HeadPitch", y, speed)
		return self

	def head_move_1(self):
		names = ["HeadYaw", "HeadPitch"]
		angleLists = [[1.0, 0.0], [0.4, 0.0, 0.1]]
		times = [[3, 5], [4, 5, 6]]
		isAbsolute = True
		self.motion_service.angleInterpolation(names, angleLists, times, isAbsolute)
		return self

	# http://doc.aldebaran.com/2-4/naoqi/motion/control-joint.html :: angleInterpolation
	def move_head_left(self, speed = 1.0):
		names = ["HeadYaw", "HeadPitch"]
		angleLists = [[1.0], [0.0]]
		times = [[speed], [speed]]
		isAbsolute = True
		self.motion_service.angleInterpolation(names, angleLists, times, isAbsolute)

		return self

	# http://doc.aldebaran.com/2-4/naoqi/motion/control-joint.html :: angleInterpolation
	def move_head_right(self, speed = 1.0):
		names = ["HeadYaw", "HeadPitch"]
		angleLists = [[-1.0], [0.0]]
		times = [[speed], [speed]]
		isAbsolute = True
		self.motion_service.angleInterpolation(names, angleLists, times, isAbsolute)

		return self

	# http://doc.aldebaran.com/2-4/naoqi/motion/control-joint.html :: angleInterpolation
	def move_head_center(self, speed = 1.0):
		names = ["HeadYaw", "HeadPitch"]
		angleLists = [[0.0], [0.0]]
		times = [[speed], [speed]]
		isAbsolute = True
		self.motion_service.angleInterpolation(names, angleLists, times, isAbsolute)

		return self

	def set_hand(self, side, shoulder_pitch = None, shoulder_roll = None, speed = 0.3, wait_time = None):
		# determine the arm to rotate
		if side in ['left', 'l', 'lf', 'lft']:
			side = 'L'
		else:
			side = 'R'

		self.motion_service.setStiffnesses("Arms", 1)
		if shoulder_pitch:
			self.motion_service.setAngles(side + "ShoulderPitch", shoulder_pitch, speed)
		if wait_time:
			time.sleep(wait_time)
		if shoulder_roll:
			self.motion_service.setAngles(side + "ShoulderRoll", shoulder_roll, speed)
		return self

	def rotate_wrist(self, side, rotation = 1.0, speed = 0.3):
		# determine the wrist to rotate
		if side in ['left', 'l', 'lf', 'lft']:
			side = 'L'
		else:
			side = 'R'

		self.motion_service.setAngles(side + "WristYaw", rotation, speed)
		return self

	def move_elbow(self, side, rotation = 1.0, speed = 0.3):
		# determine the wrist to rotate
		if side in ['left', 'l', 'lf', 'lft']:
			side = 'L'
		else:
			side = 'R'

		self.motion_service.setAngles(side + "ElbowRoll", rotation, speed)
		return self

	def rotate_elbow(self, side, rotation = 1.0, speed = 0.3):
		# determine the wrist to rotate
		if side in ['left', 'l', 'lf', 'lft']:
			side = 'L'
		else:
			side = 'R'

		self.motion_service.setAngles(side + "ElbowYaw", rotation, speed)
		return self

	def arm_up(self, side, speed = 0.3):
		return self.set_hand(side, -1, 0, speed)

	def arm_down(self, side, speed = 0.3):
		return self.set_hand(side, 1, 0, speed)

	def rotate_right(self):
		self.motion_service.moveTo(0, 0, -1.57)
		#self.motion_service.waitUntilMoveIsFinished()

		return self

	def rotate_left(self):
		self.motion_service.moveTo(0, 0, -1.57)
		#self.motion_service.waitUntilMoveIsFinished()

		return self

	def rotate_halfway(self):
		self.motion_service.moveTo(0, 0, -1.57 * 2)
		return self

	def rotate_halfway_back(self):
		self.motion_service.moveTo(0, 0, 1.57 * 2)
		return self

	'''def wave(self):
		#self.motion_service.setStiffnesses("Arms", 0.1)

		# Move arm up
		self.set_hand("right", -1, 0, 0.3)
		time.sleep(1)
		self.rotate_wrist("right", -1.3, 0.3)
		time.sleep(2)

		# Move arm to outside
		self.set_hand("right", -1, -0.6, 0.1)
		time.sleep(1)

		# Move arm to inside
		self.set_hand("right", -1, 0.3, 0.1)
		time.sleep(1)

		# Move arm to outside
		self.set_hand("right", -1, -0.6, 0.1)
		time.sleep(1)

		# Move arm to inside
		self.set_hand("right", -1, 0.3, 0.1)
		time.sleep(1)

		# Move arm to outside
		self.set_hand("right", -1, -0.6, 0.1)
		time.sleep(1)

		# Move arm to inside
		self.set_hand("right", -1, 0.3, 0.1)
		time.sleep(1)

		# back to begin position
		self.posture_service.goToPosture("StandInit", 0.5)
		self.set_head(0, 0)
		return self'''

	def wave(self):
		self.animation_service.run("animations/Stand/Gestures/Hey_1")

	def dab(self):

		self.set_hand("left", -1.5, 3, 1)
		self.set_head(-1, 0.4)
		self.set_hand("right", -0.3, 0, 0.3)
		self.move_elbow("right", 2.5, 0.3)

		time.sleep(.5)

		self.rotate_elbow("right", 0.5, 0.3)
		#time.sleep(.5)

		time.sleep(3)

		# back to begin position
		self.posture_service.goToPosture("StandInit", 0.5)
		self.set_head(0, 0)

		return self

	def move(self):
		print("move")

	def move_head(self):
		# Shake the head from side to side
		names = "HeadYaw"
		angleLists = [1.0, -1.0, 1.0, -1.0, 0.0]
		times = [1.0, 2.0, 3.0, 4.0, 5.0]
		isAbsolute = True
		self.motion_service.angleInterpolation(names, angleLists, times, isAbsolute)

		return self

	# Choose from: http://doc.aldebaran.com/2-4/naoqi/motion/alanimationplayer-advanced.html#animationplayer-list-behaviors-pepper
	def run(self, animation_file, delay = None):
		if delay:
			time.sleep(delay)
		self.animation_service.run(animation_file)