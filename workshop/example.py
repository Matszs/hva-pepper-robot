import qi

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

    def set_name(self, name):
        system = self.session.service("ALSystem")
        system.setRobotName(name)

def main():
    robot = Robot("PADrick")
    robot.connect("145.109.227.50", 9559)
    robot.set_name("Corona")

if __name__ == '__main__':
    main()