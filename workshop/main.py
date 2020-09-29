import qi
import naoqi
import sys
import motion
import time
from naoqi import *
from naoqi import ALProxy


class Robot:
    name = None
    session = None

    def __init__(self, name):
        self.name = name

    def connect(self, ip, port):
        self.session = qi.Session()
        try:
            self.session.connect("tcp://" + ip + ":" + str(port))
        except RuntimeError:
            print("Cannot connect to robot!")

    def say(self, text):
        ttsProxy = self.session.service("ALTextToSpeech")
        ttsProxy.say(text)

    def walk(self, x, y, z):
        motionProxy = self.session.service("ALMotion")
        motionProxy.moveInit()
        motionProxy.post.moveTo(x, y, z)


    def stiffness(self, stifness ):
        motionProxy = self.session.service("ALMotion")
        motionProxy.setStiffnesses("Body", stifness)

    def poses(self, posture, speed):
        postureProxy = self.session.service("ALRobotPosture")
        postureProxy.goToPosture(posture, speed)

    def joints(self, names, times, repeat):
        motionProxy = self.session.service("ALMotion")
        motionProxy.angleInterpolation(names, [0.0, 2.0], times, True)

        for i in range(repeat):
            motionProxy.angleInterpolation(names, [0.0, 2.0857], times, True)
            # motionProxy.angleInterpolation(names, [0.0, -2.0], times, True)

        # motionProxy.angleInterpolation(names, [0.0, 0.0], times, True)

def main():
    robot = Robot("Padrick")
    robot.connect("127.0.0.1", 50028)
    robot.stiffness(1.0)
    robot.walk(-0.2, 0.0, 0.0)
    robot.say("ooof")
    # robot.poses("StandZero*", 0.5)
    robot.joints(['LShoulderPitch', 'LShoulderRoll'], [[0.3], [0.3]], 1)
    robot.joints(['RShoulderPitch', 'RShoulderRoll'], [[0.3], [0.3]], 1)
    time.sleep(3000)




if __name__ == '__main__':
    main()