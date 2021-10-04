import time

class System:
	session = system_service = behavior_service = memory_service = None

	def __init__(self, session):
		self.session = session
		self.system_service = self.session.service("ALSystem")
		self.behavior_service = self.session.service("ALBehaviorManager")
		self.memory_service = self.session.service("ALMemory")
		self.run_application()

	def run_application(self):
		#do things
		return self

	def wait_on_touch(self):
		while True:
			body_parts = self.memory_service.getData("TouchChanged")
			for body_part_object in body_parts:
				part = body_part_object[0]
				touched = body_part_object[1]

				if part == 'Head/Touch/Front' or part == 'Head/Touch/Middle' or part == 'Head/Touch/Rear': # check if head is touched
					if touched:
						return self
			time.sleep(.5)

	def rename(self, name):
		self.system_service.setRobotName(name)
		return self

	def reboot(self):
		self.system_service.reboot()
		return self

	def shutdown(self):
		self.system_service.shutdown()
		return self