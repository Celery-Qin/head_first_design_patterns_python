class Light():
    def __init__(self,name):
        self.name = name

    def on(self):
        print('The light is on.')

    def off(self):
        print('The light is off.')


class GarageDoor():
    def __init__(self,name):
        self.name = name

    def up(self):
        print('The garage door is open.')

    def down(self):
        print('The garage door is close.')
    # stop()
    # light_on()
    # light_off()


class CeilingFan():
    status_high = 3
    status_medium = 2
    status_low = 1
    status_off = 0

    def __init__(self,location):
        self.location = location
        self.speed = self.status_off

    def set_status_high(self):
        self.speed = self.status_high
        print('The ceiling fan is set in speed of high.')

    def set_status_medium(self):
        self.speed = self.status_medium
        print('The ceiling fan is set in speed of medium.')

    def set_status_low(self):
        self.speed = self.status_low
        print('The ceiling fan is set in speed of low.')

    def set_status_off(self):
        self.speed = self.status_off
        print('The ceiling fan is off.')


class Stereo():
    def __init__(self,name):
        self.name = name

    def on(self):
        print('The stereo is on.')

    def set_CD(self):
        print('The CD has put into the stereo.')

    def set_volumn(self,volumn):
        print('Set the volumn to level ' + str(volumn) + '.')

    def off(self):
        print('The stereo is off.')

