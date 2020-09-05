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
        for line in ifile:
            parameters = line.split(" ")
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

    for i in range(len(gcode.commands)):
        print(gcode.commands[i][0] + " X: " + gcode.commands[i][1] + " Y: " + gcode.commands[i][2] + " Z: " + gcode.commands[i][3] + " Feed Rate: " + gcode.commands[i][4] + " Extrude: " + gcode.commands[i][5])

main()