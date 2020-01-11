import appliance_class, command_class, remote_control_class

if __name__ == '__main__':
    light_in_livingroom = appliance_class.Light('Living Room')
    light_in_livingroom_on_command = command_class.LightOnCommand(light_in_livingroom)
    light_in_livingroom_off_command = command_class.LightOffCommand(light_in_livingroom)

    light_in_kitchen = appliance_class.Light('Kitchen')
    light_in_kitchen_on_command = command_class.LightOnCommand(light_in_kitchen)
    light_in_kitchen_off_command = command_class.LightOffCommand(light_in_kitchen)

    garage_door = appliance_class.GarageDoor('Garage Door')
    garage_door_open_command = command_class.GarageDoorOpenCommand(garage_door)
    garage_door_close_command = command_class.GarageDoorCloseCommand(garage_door)

    ceiling_fan = appliance_class.CeilingFan('Living Room')  # speed = 0
    ceiling_fan_high_command = command_class.CeilingFanHighCommand(ceiling_fan)
    ceiling_fan_medium_command = command_class.CeilingFanMediumCommand(ceiling_fan)
    ceiling_fan_low_command = command_class.CeilingFanLowCommand(ceiling_fan)
    ceiling_fan_off_command = command_class.CeilingFanOffCommand(ceiling_fan)
    
    stereo = appliance_class.Stereo('Stereo')
    stereo_on_command = command_class.StereoOnWithCDCommand(stereo)
    stereo_off_command = command_class.StereoOffCommand(stereo)

    party_on_commands = command_class.PartyCommand(light_in_livingroom_on_command,ceiling_fan_medium_command,stereo_on_command)
    party_off_commands = command_class.PartyCommand(light_in_livingroom_off_command,ceiling_fan_off_command,stereo_off_command)

    remote_control = remote_control_class.RemoteControl()

    remote_control.set_command(0, light_in_livingroom_on_command, light_in_livingroom_off_command)
    remote_control.set_command(1, light_in_kitchen_on_command, light_in_kitchen_off_command)
    remote_control.set_command(2, garage_door_open_command, garage_door_close_command)
    remote_control.set_command(3, ceiling_fan_high_command, ceiling_fan_medium_command)
    remote_control.set_command(4, stereo_on_command, stereo_off_command)
    remote_control.set_command(5, ceiling_fan_low_command, ceiling_fan_off_command)
    remote_control.set_command(6, party_on_commands, party_off_commands)
    
    print(remote_control)
    # output:
    # ------ Remote Control ------
    # Slot: 0<class 'command_class.LightOnCommand'><class 'command_class.LightOffCommand'>
    # Slot: 1<class 'command_class.LightOnCommand'><class 'command_class.LightOffCommand'>
    # Slot: 2<class 'command_class.GarageDoorOpenCommand'><class 'command_class.GarageDoorCloseCommand'>
    # Slot: 3<class 'command_class.CeilingFanHighCommand'><class 'command_class.CeilingFanMediumCommand'>
    # Slot: 4<class 'command_class.StereoOnWithCDCommand'><class 'command_class.StereoOffCommand'>
    # Slot: 5<class 'command_class.CeilingFanLowCommand'><class 'command_class.CeilingFanOffCommand'>
    # Slot: 6<class 'command_class.NoCommand'><class 'command_class.NoCommand'>

    # print('Print initial remote control undo():')
    # remote_control.undo_button_pressed()
    # output:
    # Print initial remote control undo():
    # There is nothing to undo.

    print('Try every button:')
    for i in range(7):
        print('Slot ' + str(i) + ':')
        remote_control.on_button_pressed(i)
        remote_control.off_button_pressed(i)
    # output:
    # Try every button:
    # Slot 0:
    # The light is on.
    # The light is off.
    # Slot 1:
    # The light is on.
    # The light is off.
    # Slot 2:
    # The garage door is open.
    # The garage door is close.
    # Slot 3:
    # The ceiling fan is set in speed of high.
    # The ceiling fan is set in speed of medium.
    # Slot 4:
    # The stereo is on.
    # The CD has put into the stereo.
    # Set the volumn to level 11.
    # The stereo is off.
    # Slot 5:
    # The ceiling fan is set in speed of low.
    # The ceiling fan is off.
    
    remote_control.undo_button_pressed()