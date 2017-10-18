"""This is the main assembler module used to generate the object code and hex file"""
import sys
import MachineCodeBuilder

if len(sys.argv) < 2:
    print("Source file not specified.")
    sys.exit()

filename = sys.argv[1].split(".")[0]

# Concatenate each line (binary) to machine_code
machine_code = ""

try:
    with open(sys.argv[1], "r") as source_file:
        with open("{}.o".format(filename), "wb") as bin_file:
            with open("{}.psd".format(filename), "w") as hex_file:
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
                        label = int(args[0])

                        machine_code_result = MachineCodeBuilder.build_J_type(2,label)
                        bin_file.write(machine_code_result[0])
                        hex_file.write("{}\n".format(machine_code_result[1]))
                        print("[J] ins=\"%s\", op=%s, label=%s" % (line, op, label))

                    # I type - 3 args (e.g., beq)
                    elif op == "beq":
                        rs = int(args[0][1:])
                        rt = int(args[1][1:])
                        imm = int(args[2])

                        machine_code_result = MachineCodeBuilder.bulid_I_type(4,rs,rt,imm)
                        bin_file.write(machine_code_result[0])
                        hex_file.write("{}\n".format(machine_code_result[1]))
                        print("[I] ins=\"%s\", op=%s, rs=%s, rt=%s, imm=%s " % (line, op, rs, rt, imm))

                    # I type - 2 args (e.g., lwd, swd)
                    elif op == "lwd" or op == "swd":
                        rt = int(args[0][1:])
                        offset = int(args[1][:args[1].index('(')])
                        rs = int(args[1][args[1].index('(')+1:args[1].index(')')][1:])

                        if op == "lwd":
                            op_code = 35
                        else:
                            op_code = 43
                        
                        machine_code_result = MachineCodeBuilder.bulid_I_type(op_code,rs,rt,offset)
                        bin_file.write(machine_code_result[0])
                        hex_file.write("{}\n".format(machine_code_result[1]))
                        print("[I] ins=\"%s\", op=%s, rd=%s, offset=%s, rs=%s" % (line, op, rt, offset, rs))

                    # R type
                    elif op == "add" or op == "sub" or op == "slt" or op == "and" or op == "nor":
                        rd = int(args[0][1:])
                        rs = int(args[1][1:])
                        rt = int(args[2][1:])

                        if op == "add":
                            op_code = 10
                        elif op == "sub":
                            op_code = 20
                        elif op == "slt":
                            op_code = 30
                        elif op == "and":
                            op_code = 40
                        elif op == "nor":
                            op_code = 50

                        machine_code_result = MachineCodeBuilder.build_R_type(op_code,rs,rt,rd,0,0)
                        bin_file.write(machine_code_result[0])
                        hex_file.write("{}\n".format(machine_code_result[1]))
                        print("[R] ins=\"%s\", op=%s, rd=%s, rs=%s, rt=%s" % (line, op, rd, rs, rt))

                    # Not supported
                    else:
                        print("Instruction %s not supported" % (line))
                        sys.exit()


except IOError:
    print("File IO Error")
    sys.exit()


# Write out machine_code to file
# Convert machine_code to hexstring and write to file