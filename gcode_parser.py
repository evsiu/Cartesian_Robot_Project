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

            gcode_check = parameters[0]
            self.x = parameters[1][1:]
            self.y = parameters[2][1:]
            self.z = parameters[3][1:]

            self.feed_rate = parameters[4][1:]
            self.extrude = parameters[5][1:]
            command_arguments = [self.x, self.y, self.z, self.feed_rate, self.extrude]
            #print("X: " + self.x + " Y: " + self.y + " Z: " + self.z + " Feed Rate: " + self.feed_rate + " Extrude: " + self.extrude)
            self.commands.append(command_arguments)

#def main():
#    input_file = "test.txt"
#    gcode = GCODE_PARSE(input_file)
#    gcode.parse()
#
#    for i in range(len(gcode.commands)):
#        print("X: " + gcode.commands[i][0] + " Y: " + gcode.commands[i][1] + " Z: " + gcode.commands[i][2] + " Feed Rate: " + gcode.commands[i][3] + " Extrude: " + gcode.commands[i][4])
#
#main()