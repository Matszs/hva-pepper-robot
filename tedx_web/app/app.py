# coding=utf-8
# error log; tail -f /var/log/naoqi/servicemanager/system.Naoqi_error.log
# Debug log; tail -f /var/log/naoqi/servicemanager/system.Naoqi.log
# Autoload on boot; nano /home/nao/naoqi/preferences/autoload.ini
# nohup python app.py &
# kill $(ps aux | grep 'app.py' | awk '{print $2}')
from mirai import Mirai
import time
import threading
import argparse
import datetime

DEFAULT_TEXT_SPEED = 100 # 50 - 400
mirai = None
TEX_OR_FLOOR = 1 # 1 = tex, 2 = floor

def tedx():
	mirai.speech().set_language("English")
	mirai.speech().set_pitch(1.3)
	mirai.speech().set_speed(90)
	mirai.speech().asay(
		"^mode(disabled) ^start(animations/Stand/Gestures/Hey_1) Hello my name is Mirai. On behalf of the Amsterdam University ^wait(animations/Stand/Gestures/Hey_1) ^mode(contextual) of Applied Sciences I would like to welcome you to the first TED X H V Amsterdam. Enjoy!")

	time.sleep(1)
	mirai.speech().asay(
		"^mode(disabled) ^start(animations/Stand/Gestures/Explain_4) You look great by the way. ^wait(animations/Stand/Gestures/Explain_4) ^mode(contextual)")

	mirai.motion().move_head_bit_up()
	time.sleep(1)
	mirai.motion().stand(0.5)

def floor():
	mirai.speech().set_language("English")
	mirai.speech().set_pitch(1.3)
	mirai.speech().set_speed(80)
	mirai.speech().asay("^mode(disabled) ^start(animations/Stand/Gestures/Hey_1) Hello my name Mirai! And I am the robot of the hbo-i cee tea programme here at the Amsterdam University of Applied Sciences. ^wait(animations/Stand/Gestures/Hey_1) ^mode(contextual)")

	mirai.speech().asay("I am a robot that is programmed by hbo-i cee tea students for healthcare. ")

	threading.Thread(target=mirai.tablet().open_page, args=("tedx_video.html",)).start()
	mirai.speech().asay("During the hbo-i cee tea training we work on solutions for societal challenges of the future with technologies such as virtual and augmented reality, blockchain, artificial intelligence and quantum computing.")

	mirai.motion().run('animations/Stand/Gestures/ShowTablet_2')

	time.sleep(3)
	mirai.motion().stand(0.5)
	mirai.tablet().open_page("tedx_default.html?time=123")

	mirai.speech().asay("Visit our website www.hva.nl/hbo-i cee tea for more information about the training. Or visit one of these events:")
	mirai.motion().run('animations/Stand/Gestures/ShowTablet_1')
	mirai.tablet().open_page("tedx_digivita.html")
	time.sleep(6)
	mirai.tablet().open_page("tedx_quantum.html")
	time.sleep(6)

	mirai.tablet().open_page("tedx_default.html?time=123")
	mirai.motion().stand(0.5)


def on_face_detected_callback(count):
	print("face detected: " + str(count))
	if TEX_OR_FLOOR == 2:
		floor()
	else:
		tedx()

def program():
	mirai.start()
	print("Program started")

	mirai.tablet().open_page("tedx_default.html?time=123")
	mirai.speech().set_volume(1.0).set_voice("naoenu").set_language("English")

	mirai.face_detection().set_on_face_detected_callback(on_face_detected_callback)
	if TEX_OR_FLOOR == 1:
		mirai.face_detection().set_timeout(40000) # 2 minutes
	else:
		mirai.face_detection().set_timeout(120000) # 2 minutes

	mirai.face_detection().start_detection()

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("--pip", type=str, default="127.0.0.1", help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
	parser.add_argument("--pport", type=int, default=9559, help="Naoqi port number")

	args = parser.parse_args()

	mirai = Mirai(args.pip, args.pport)

	program()

