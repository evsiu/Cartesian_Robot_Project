def parse(input_file):
    #parse the input file
    ifile = open(input_file, "r")
    for line in ifile:
        parameters = line.split(" ")

        gcode_check = parameters[0]
        x = parameters[1][1:]
        y = parameters[2][1:]
        z = parameters[3][1:]

        feed_rate = parameters[4][1:]
        extrude = parameters[5][1:]
        print("X: " + x + " Y: " + y + " Z: " + z + " Feed Rate: " + feed_rate + " Extrude: " + extrude)

def main():
    input_file = "test.txt"
    parse(input_file)

main()