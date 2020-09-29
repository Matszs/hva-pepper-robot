# coding=utf-8
# error log; tail -f /var/log/naoqi/servicemanager/system.Naoqi_error.log
# Debug log; tail -f /var/log/naoqi/servicemanager/system.Naoqi.log
# Autoload on boot; nano /home/nao/naoqi/preferences/autoload.ini
# nohup python app.py &
# kill $(ps aux | grep 'app.py' | awk '{print $2}')
# http://145.109.225.252/advanced/

from mirai_lib import Mirai
import time
import threading
import argparse
import datetime
from services.remote_control_service import RemoteControlService

class RemoteControl:
    mirai = None
    def __init__(self, mirai):
        self.mirai = mirai

    def on_command(self, cmd):
        print(cmd)

        if cmd == 'up':
            self.mirai.motion().walk_forward()
        if cmd == 'up2':
            self.mirai.motion().walk_forward_long()
        elif cmd == 'down':
            self.mirai.motion().walk_backward()
        elif cmd == 'left':
            self.mirai.motion().walk_left()
        elif cmd == 'right':
            self.mirai.motion().walk_right()
        elif cmd == 'stand':
            self.mirai.motion().stand()
        elif cmd == 'sleep':
            self.mirai.motion().sleep()
        elif cmd == 'speak-1':
            #self.mirai.speech().set_pitch(1.1).set_speed(100).asay('nou Somaya, hartstikke leuk allemaal, maar laten we nu weer aan het werk gaan!')
            self.mirai.speech().set_pitch(1.1).set_speed(75).asay('Dank voor je verhaal Somaya. Ik vind het fijn om te horen dat wij nog lang samen kunnen werken. Dat doe je al sinds 2008 met mijn voorgangers, maar ik vind toch wel erg fijn dat ik steeds meer tot jouw favoriete robot behoor. Rest mij niets meer dan je veel succes te wensen voor de toekomst.')
            self.mirai.motion().run("animations/Stand/Gestures/Hey_1")
        else:
            self.mirai.motion().stop_walking()

    def on_start(self):
        self.mirai.speech().set_volume(1.0).set_language("Dutch").set_speed(100)
        self.mirai.tablet().open_page('remote_control/default.html?time=12454546777')
        self.program()

    def program(self):
        print("Program started")

        self.mirai.register_service('remoteControl', RemoteControlService())
        remote_control_service = self.mirai.session.service('remoteControl')
        remote_control_service.onCommand.connect(self.on_command)

        self.mirai.motion().disable_collision_protection()
        #self.mirai.motion().walk()
        while True:
            time.sleep(.1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--pport", type=int, default=9559, help="Naoqi port number")

    args = parser.parse_args()
    mirai = Mirai(args.pip, args.pport)

    mirai.start(False) # True = Wait on head touch to start application
    application = RemoteControl(mirai)
    application.on_start()


if __name__ == '__main__':
    main()
