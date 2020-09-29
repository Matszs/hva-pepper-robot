import qi


class RemoteControlService:
    def __init__(self, *args, **kwargs):
        self.onCommand = qi.Signal()

    def command(self, value):
        self.onCommand(value)
