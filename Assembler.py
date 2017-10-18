"""This is the main assembler module used to generate the object code and hex file"""
import sys

if len(sys.argv) < 2:
    print("Source file not specified.")
    sys.exit()

# Concatenate each line (binary) to machine_code
machine_code = ""

try:
    with open(sys.argv[1], "r") as source_file:
        for line in source_file:
            line = line.lower().strip()

            # TODO:
            # Validate input (e.g., no $x for registers--just numbers 0 to 31).
            # Also validate within each op case to ensure the proper arguments are met.

            op = line.split()[0]
            # print "op=%s" % (op)
            # removes all whitespaces prior to converting to comma delimited array
            args = ''.join(line.split()[1:]).split(',')
            # print "args=%s" % (args)

            # J type
            if op == "j":
                label = args[0]
                print "[J] ins=\"%s\", op=%s, label=%s" % (line, op, label)

            # I type - 3 args (e.g., beq)
            elif op == "beq":
                rs = args[0]
                rt = args[1]
                imm = args[2]
                print "[I] ins=\"%s\", op=%s, rs=%s, rt=%s, imm=%s " % (line, op, rs, rt, imm)

            # I type - 2 args (e.g., lwd, swd)
            elif op == "lwd" or op == "swd":
                rd = args[0]
                offset = args[1][:args[1].index('(')]
                rs = args[1][args[1].index('(')+1:args[1].index(')')]
                print "[I] ins=\"%s\", op=%s, rd=%s, offset=%s, rs=%s" % (line, op, rd, offset, rs)

            # R type
            elif op == "add" or op == "sub" or op == "slt" or op == "and" or op == "nor":
                rd = args[0]
                rs = args[1]
                rt = args[2]
                print "[R] ins=\"%s\", op=%s, rd=%s, rs=%s, rt=%s" % (line, op, rd, rs, rt)

            # Not supported
            else:
                print "Instruction %s not supported" % (line)


except IOError:
    print("File IO Error")
    sys.exit()


# Write out machine_code to file
# Convert machine_code to hexstring and write to file