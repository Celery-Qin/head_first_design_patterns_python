import appliance_class

class Command():
    def execute(self):
        pass

    def undo(self):
        pass


class NoCommand(Command):
    def execute(self):
        print('There is no command.')

    def undo(self):
        print('There is nothing to undo.\n')


class LightOnCommand(Command, appliance_class.Light):
    def __init__(self,light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()


class LightOffCommand(Command, appliance_class.Light):
    def __init__(self,light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()

class GarageDoorOpenCommand(Command, appliance_class.GarageDoor):
    def __init__(self, garage_door):
        self.garage_door = garage_door

    def execute(self):
        self.garage_door.up()

    def undo(self):
        self.garage_door.down()


class GarageDoorCloseCommand(Command, appliance_class.GarageDoor):
    def __init__(self, garage_door):
        self.garage_door = garage_door

    def execute(self):
        self.garage_door.down()

    def undo(self):
        self.garage_door.up()


# class CeilingFanOnCommand(Command, appliance_class.CeilingFan):
#     def __init__(self, ceiling_fan):
#         self.ceiling_fan = ceiling_fan

#     def execute(self):
#         self.ceiling_fan.on()

#     def undo(self):
#         self.ceiling_fan.off()


# class CeilingFanOffCommand(Command, appliance_class.CeilingFan):
#     def __init__(self, ceiling_fan):
#         self.ceiling_fan = ceiling_fan

#     def execute(self):
#         self.ceiling_fan.off()

#     def undo(self):
#         self.ceiling_fan.on()


class CeilingFanHighCommand(Command,appliance_class.CeilingFan):
    def __init__(self, ceiling_fan):
        self.ceiling_fan = ceiling_fan
        self.prev_speed = ceiling_fan.speed

    def execute(self):
        self.prev_speed = self.ceiling_fan.speed
        self.ceiling_fan.set_status_high()

    def undo(self):
        if self.prev_speed == appliance_class.CeilingFan.status_high:
            self.ceiling_fan.set_status_high()
        elif self.prev_speed == appliance_class.CeilingFan.status_medium:
            self.ceiling_fan.set_status_medium()
        elif self.prev_speed == appliance_class.CeilingFan.status_low:
            self.ceiling_fan.set_status_low()
        else:
            self.ceiling_fan.set_status_off()


class CeilingFanMediumCommand(Command,appliance_class.CeilingFan):
    def __init__(self, ceiling_fan):
        self.ceiling_fan = ceiling_fan
        self.prev_speed = ceiling_fan.speed

    def execute(self):
        self.prev_speed = self.ceiling_fan.speed
        self.ceiling_fan.set_status_medium()

    def undo(self):
        if self.prev_speed == appliance_class.CeilingFan.status_high:
            self.ceiling_fan.set_status_high()
        elif self.prev_speed == appliance_class.CeilingFan.status_medium:
            self.ceiling_fan.set_status_medium()
        elif self.prev_speed == appliance_class.CeilingFan.status_low:
            self.ceiling_fan.set_status_low()
        else:
            self.ceiling_fan.set_status_off()


class CeilingFanLowCommand(Command,appliance_class.CeilingFan):
    def __init__(self, ceiling_fan):
        self.ceiling_fan = ceiling_fan
        self.prev_speed = ceiling_fan.speed

    def execute(self):
        self.prev_speed = self.ceiling_fan.speed
        self.ceiling_fan.set_status_low()

    def undo(self):
        if self.prev_speed == appliance_class.CeilingFan.status_high:
            self.ceiling_fan.set_status_high()
        elif self.prev_speed == appliance_class.CeilingFan.status_medium:
            self.ceiling_fan.set_status_medium()
        elif self.prev_speed == appliance_class.CeilingFan.status_low:
            self.ceiling_fan.set_status_low()
        else:
            self.ceiling_fan.set_status_off()

class CeilingFanOffCommand(Command,appliance_class.CeilingFan):
    def __init__(self, ceiling_fan):
        self.ceiling_fan = ceiling_fan
        self.prev_speed = ceiling_fan.speed

    def execute(self):
        self.prev_speed = self.ceiling_fan.speed
        self.ceiling_fan.set_status_off()

    def undo(self):
        if self.prev_speed == appliance_class.CeilingFan.status_high:
            self.ceiling_fan.set_status_high()
        elif self.prev_speed == appliance_class.CeilingFan.status_medium:
            self.ceiling_fan.set_status_medium()
        elif self.prev_speed == appliance_class.CeilingFan.status_low:
            self.ceiling_fan.set_status_low()
        else:
            self.ceiling_fan.set_status_off()


class StereoOnWithCDCommand(Command, appliance_class.Stereo):
    def __init__(self, stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.on()
        self.stereo.set_CD()
        self.stereo.set_volumn(11)

    def undo(self):
        self.stereo.off()


class StereoOffCommand(Command, appliance_class.Stereo):
    def __init__(self, stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.off()

    def undo(self):
        self.stereo.on()
        self.stereo.set_CD()
        self.stereo.set_volumn(11)

        
class PartyCommand(Command):
    def __init__(self, *command):
        self.commands = [*command]

    def execute(self):
        for command in self.commands:
            command.execute()

    def undo(self):
        for command in self.commands:
            command.undo()