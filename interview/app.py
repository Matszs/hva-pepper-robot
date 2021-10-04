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


class Interview:
    mirai = None
    def __init__(self, mirai):
        self.mirai = mirai

    def on_start(self):
        self.program()

    def program(self):
        print("Program started")

        self.mirai.speech().set_volume(1.0).set_language("Dutch").set_speed(100)



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--pport", type=int, default=54447, help="Naoqi port number")

    args = parser.parse_args()
    mirai = Mirai(args.pip, args.pport)

    mirai.start(False) # True = Wait on head touch to start application
    application = Interview(mirai)
    application.on_start()


if __name__ == '__main__':
    main()
