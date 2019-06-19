import time
import threading
import qi


class FaceDetection:
	session = face_detection_service = memory_service = None
	detection_started = False
	on_face_detected_callback = None
	time_out_time = 0
	last_time_detected = None

	def __init__(self, session):
		self.session = session
		self.face_detection_service = self.session.service("ALFaceDetection")
		self.memory_service = self.session.service("ALMemory")

	def process_face_detection(self):
		while self.detection_started:
			time.sleep(0.5)
			val = self.memory_service.getData("FaceDetected", 0)

			# Check if we find some face
			if val and isinstance(val, list) and len(val) > 0:
				# We detected faces !
				# For each face, we can read its shape info and ID.
				# First Field = TimeStamp.
				timeStamp = val[0]
				# Second Field = array of face_Info's.
				faceInfoArray = val[1]

				if not self.detection_started:
					false

				if self.time_out_time > 0 and self.last_time_detected and ((self.last_time_detected / 1000000) + self.time_out_time) > (qi.systemClockNow() / 1000000):
					continue

				face_count = len(faceInfoArray) - 1

				self.last_time_detected = qi.systemClockNow()

				if self.on_face_detected_callback:
					self.on_face_detected_callback(face_count)

				'''try:
					# Browse the faceInfoArray to get info on each detected face.
					for faceInfo in faceInfoArray:

						print(faceInfo)

						# First Field = Shape info.
						faceShapeInfo = faceInfo[0]
						# Second Field = Extra info (empty for now).
						faceExtraInfo = faceInfo[1]
						print("  alpha %.3f - beta %.3f" % (faceShapeInfo[1], faceShapeInfo[2]))
						print("  width %.3f - height %.3f" % (faceShapeInfo[3], faceShapeInfo[4]))
				except Exception, e:
					#print("faces detected, but it seems getData is invalid. ALValue =")
					#print(val)
					#print("Error msg %s" % (str(e)))
					continue'''


	def start_detection(self):
		self.face_detection_service.setTrackingEnabled(False)
		self.face_detection_service.subscribe("Test_Face", 500, 0.0)
		self.detection_started = True

		threading.Thread(target=self.process_face_detection).start()

	def set_on_face_detected_callback(self, callback):
		self.on_face_detected_callback = callback

	def set_timeout(self, time):
		self.time_out_time = time

	def stop_detection(self):
		self.detection_started = False