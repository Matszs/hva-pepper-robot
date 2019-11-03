import time
import threading


class WavingDetection:
	session = waving_detection_service = memory_service = tracker = None
	detection_started = False

	def __init__(self, session):
		self.session = session
		self.waving_detection_service = self.session.service("ALWavingDetection")
		self.memory_service = self.session.service("ALMemory")
		self.tracker = self.session.service("ALTracker")


	def start_detection(self):
		self.tracker.setMode("Head")


		#self.waving_detection_service.subscribe("WavingDetection", 500, 0.0)


		while True:
			time.sleep(0.5)
			val = self.memory_service.getData("WavingDetection/Waving", 0) #298109
			print(val)

	def stop_detection(self):
		self.detection_started = False