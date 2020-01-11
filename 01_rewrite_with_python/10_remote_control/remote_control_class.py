import command_class

class RemoteControl():
    def __init__(self):
        no_command = command_class.NoCommand()
        self.undo_command = no_command
        self.on_command_list = [no_command] * 7
        self.off_command_list = [no_command] * 7

    def set_command(self, slot_num, on_command, off_command):
        self.on_command_list[slot_num] = on_command
        self.off_command_list[slot_num] = off_command

    def on_button_pressed(self, slot_num):
        self.undo_command = self.on_command_list[slot_num]
        self.on_command_list[slot_num].execute()
        

    def off_button_pressed(self, slot_num):
        self.undo_command = self.off_command_list[slot_num]
        self.off_command_list[slot_num].execute()
        

    def undo_button_pressed(self):
        self.undo_command.undo()
        
    def __str__(self):
        string_buff = '\n------ Remote Control ------\n'
        for i in range(7):
            string_buff += 'Slot: ' + str(i)
            string_buff += str(self.on_command_list[i].__class__)
            string_buff += str(self.off_command_list[i].__class__)
            string_buff += '\n'
        return string_buff