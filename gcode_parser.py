class GCODE_PARSE:
    def __init__(self, input_file):
        self.input_file = input_file

        self.x = 0
        self.y = 0
        self.z = 0

        self.feed_rate = 0
        self.extrude = 0
    def parse(self):
        #parse the input file

        ifile = open(self.input_file, "r")
        self.commands = []
        self.conditions = []

        self.conditions.append(str(self.input_file))
        for param_line in ifile:
            if(param_line[0:10] == ";Generated"):
                break
            else:
                self.conditions.append(param_line[1:])

        for line in ifile:
            parameters = line.split(" ")
            self.g_command = "none"
            self.x, self.y, self.z, self.feed_rate, self.extrude = "0", "0", "0", "0", "0"
            for command in parameters:
                if(command[0] == "G"):
                    self.g_command = command
                elif(command[0] == "F"):
                    self.feed_rate = command[1:]
                elif(command[0] == "X"):
                    self.x = command[1:]
                elif(command[0] == "Y"):
                    self.y = command[1:]
                elif(command[0] == "Z"):
                    self.z = command[1:]
                elif(command[0] == "E"):
                    self.extrude = command[1:]
            command_arguments = [self.g_command, self.x, self.y, self.z, self.feed_rate, self.extrude]
            #print("X: " + self.x + " Y: " + self.y + " Z: " + self.z + " Feed Rate: " + self.feed_rate + " Extrude: " + self.extrude)
            self.commands.append(command_arguments)

def main():
    input_file = "test.txt"
    gcode = GCODE_PARSE(input_file)
    gcode.parse()

    if(len(gcode.conditions) > 1):
        #for i in range(len(gcode.conditions)):
        print(gcode.conditions[0] + "\n" + gcode.conditions[2] + " " + gcode.conditions[3] + " " + gcode.conditions[4] + "\n" + gcode.conditions[5] + "\t" + gcode.conditions[8] + "\n" + gcode.conditions[6] + "\t" + gcode.conditions[9] + "\n" + gcode.conditions[7] + "\t" + gcode.conditions[10] + "\n")
    for i in range(len(gcode.commands)):
        print(gcode.commands[i][0] + " X: " + gcode.commands[i][1] + " Y: " + gcode.commands[i][2] + " Z: " + gcode.commands[i][3] + " Feed Rate: " + gcode.commands[i][4] + " Extrude: " + gcode.commands[i][5])
    

main()