class Command():
    def execute(self):
        pass

    def undo(self):
        pass


class Light():
    def on(self):
        print('The light is on.')

    def off(self):
        print('The light is off.')


class LightOnCommand(Command,Light):
    def __init__(self,light):
        self.light = light

    def execute(self):
        self.light.on()


class GarageDoor():
    def up(self):
        print('The garage door is open.')
    # down()
    # stop()
    # light_on()
    # light_off()


class GarageDoorOpenCommand(Command, GarageDoor):
    def __init__(self, garage_door):
        self.garage_door = garage_door

    def execute(self):
        self.garage_door.up()


class SimpleRemoteControl():
    def __init__(self):
        self.slot = None

    def set_command(self,command):
        self.slot = command

    def button_pressed(self):
        self.slot.execute()

# test
if __name__ == '__main__':
    light_test = Light()
    light_on_test = LightOnCommand(light_test)

    garage_door_test = GarageDoor()
    garage_door_open_test = GarageDoorOpenCommand(garage_door_test)

    remote_control_test = SimpleRemoteControl()
    remote_control_test.set_command(light_on_test)
    remote_control_test.button_pressed()

    remote_control_test = SimpleRemoteControl()
    remote_control_test.set_command(garage_door_open_test)
    remote_control_test.button_pressed()