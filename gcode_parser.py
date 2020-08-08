class Parse:
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
        for line in ifile:
            parameters = line.split(" ")

            gcode_check = parameters[0]
            self.x = parameters[1][1:]
            self.y = parameters[2][1:]
            self.z = parameters[3][1:]

            self.feed_rate = parameters[4][1:]
            self.extrude = parameters[5][1:]
            print("X: " + self.x + " Y: " + self.y + " Z: " + self.z + " Feed Rate: " + self.feed_rate + " Extrude: " + self.extrude)

#def main():
#    input_file = "test.txt"
#    gcode = Parse(input_file)
#    gcode.parse()
#
#main()