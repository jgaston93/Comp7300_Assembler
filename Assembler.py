"""This is the main assembler module used to generate the object code and hex file"""
import sys

if len(sys.argv) < 2:
    print("Source file not specified.")
    sys.exit()

try:
    with open(sys.argv[1], "r") as source_file:
        for line in source_file:
            line = line.strip()

            # This handles control transfer instructions
            if line[0].lower() == "j" or line[0].lower() == "b":
                pass
            else:
                instruction = line[0:3].lower()

                # This handles memory references/transfers
                if instruction == "lwd" or instruction == "swd":
                    pass

                # This handles arithmetic and logical instructions
                else:
                    pass


except IOError:
    print("File IO Error")
    sys.exit()
