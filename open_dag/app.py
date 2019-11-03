# coding=utf-8
# error log; tail -f /var/log/naoqi/servicemanager/system.Naoqi_error.log
# Debug log; tail -f /var/log/naoqi/servicemanager/system.Naoqi.log
# Autoload on boot; nano /home/nao/naoqi/preferences/autoload.ini
# nohup python app.py &
# kill $(ps aux | grep 'app.py' | awk '{print $2}')

from mirai_lib import Mirai
import time
import threading
import argparse
import datetime


class Opendag:
    mirai = None
    def __init__(self, mirai):
        self.mirai = mirai

    def on_start(self):
        self.mirai.tablet().open_page('open_dag/default.html')
        self.program()

    def on_face_detected_callback(self, face_count):
        self.mirai.speech().asay("Hey Hallo!")
        self.mirai.speech().asay("Welkom op de open dag van Ha b oh ie c t!")
        self.mirai.speech().asay("Wil je aan de slag met programmeren, hardware en misschien robots? Kijk dan naar de opleiding Technische Informatica!")
        self.mirai.speech().asay("Misschien zie ik je dan wel!")
        self.mirai.motion().stand()

    def program(self):
        print("Program started")

        self.mirai.speech().set_volume(1.0).set_language("Dutch").set_speed(100)

        self.mirai.face_detection().set_on_face_detected_callback(self.on_face_detected_callback)
        self.mirai.face_detection().set_timeout(40000)
        self.mirai.face_detection().start_detection()

        #self.mirai.motion().explore()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--pport", type=int, default=9559, help="Naoqi port number")

    args = parser.parse_args()
    mirai = Mirai(args.pip, args.pport)

    mirai.start(True) # True = Wait on head touch to start application
    application = Opendag(mirai)
    application.on_start()


if __name__ == '__main__':
    main()
