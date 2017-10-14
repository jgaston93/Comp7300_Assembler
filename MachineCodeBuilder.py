"""This module contains the helper functions used to build the machine code that will be written to the files"""
from struct import pack

def build_R_type(opcode, rs, rt, rd, shamt, function):
    """builds a tuple that contains a byte array and the hex string of the R-type command"""
    binary_number = function
    binary_number = binary_number << 5
    binary_number = binary_number | shamt
    binary_number = binary_number << 5
    binary_number = binary_number | rd
    binary_number = binary_number << 5
    binary_number = binary_number | rs
    binary_number = binary_number << 5
    binary_number = binary_number | rt
    binary_number = binary_number << 6
    binary_number = binary_number | opcode
    binary_number = pack('>I', binary_number)
    return (binary_number, "0x{0}".format(binary_number.hex()))

def bulid_I_type(opcode, rs, rt, constant):
    """builds a tuple that contains a byte array and the hex string of the I-type command"""
    binary_number = constant
    binary_number = binary_number << 5
    binary_number = binary_number | rs
    binary_number = binary_number << 5
    binary_number = binary_number | rt
    binary_number = binary_number << 6
    binary_number = binary_number | opcode
    binary_number = pack('>I', binary_number)
    return (binary_number, "0x{0}".format(binary_number.hex()))

def build_J_type(opcode, address):
    """builds a tuple that contains a byte array and the hex string of the J-type command"""
    binary_number = address
    binary_number = binary_number << 6
    binary_number = binary_number | opcode
    binary_number = pack('>I', binary_number)
    return (binary_number, "0x{0}".format(binary_number.hex()))

