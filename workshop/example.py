import qi
import time

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
            print ("Cannot connect to robot!")

    def say(self, text):
        textToSpeechService = self.session.service("ALTextToSpeech")
        textToSpeechService.say(text)

    def asay(self, text):
        textToSpeechService = self.session.service("ALAnimatedSpeech")
        textToSpeechService.say(text)

    def set_name(self, name):
        system = self.session.service("ALSystem")
        system.setRobotName(name)

def main():
    robot = Robot("PADrick")
    robot.connect("127.0.0.1", 55247)
    robot.asay("hoe Loes & Lies!")
    robot.asay(" Ik mis jullie! Wanneer mag ik een keer langskomen? ")

if __name__ == '__main__':
    main()