import re
from data import *
import error as er
import sys

r_type_instructions = ["add", "sub", "sll", "slt", "sltu", "xor", "srl", "or", "and"]
i_type_instructions = ["lw", "addi", "sltiu", "jalr"]
s_type_instructions = ["sw"]
b_type_instructions = ["beq", "bne", "blt", "bge", "bltu", "bgeu"]
u_type_instructions = ["lui", "auipc"]
j_type_instructions = ["jal"]
bonus = ["mul", "rst", "halt", "rvrs"]
unique_registers = ["zero", "ra", "sp", "gp", "tp", "t0", "t1", "t2", "s0", "fp", "s1", "a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "s11", "t3", "t4", "t5", "t6"]

all_instructions = r_type_instructions + i_type_encoding + s_type_encoding + b_type_instructions + u_type_instructions + j_type_instructions + bonus + unique_registers

input_file_add = input("Enter the address to the input text file: ")
file = open(input_file_add, "r")
data = file.readlines()
file.close()

binary_output = ''

l = 1

for line in data:

    line = line[:-1]
    line_data = re.split(",| ", line)               #both spaces as well as commas are used as delimiters

    p = 1

    for i in line_data:
        if line_data[0] in all_instructions:
            p = p*1
        else:
            p = p*0

    if p == 0:
        print("Error at line", i, end = " ")

        # use error.py
        # error handling code

        continue

    if line_data[0] in r_type_instructions:
        binary_output += r_type_encoding[line_data[0]]["opcode"] + registers[line_data[1]] + r_type_encoding[line_data[0]]["funct3"] + registers[line_data[2]] + registers[line_data[3]] + r_type_encoding[line_data[0]]["funct7"]

    elif line_data[0] in i_type_instructions:
        line_data[3] = bin(int(line_data[3]))
        line_data[3] = line_data[3][2:]
        binary_output += i_type_encoding[line_data[0]]["opcode"] + registers[line_data[1]] + i_type_encoding[line_data[0]]["funct3"] + registers[line_data[2]] + line_data[3]

    elif (line_data[0] in s_type_instructions):
        line_data[2] = bin(int(line_data[2]))
        line_data[2] = line_data[2][2:]
        binary_output += s_type_encoding["sw"]["opcode"] + line_data[2][0:4] + s_type_encoding["sw"]["funct3"] + registers[line_data[1]] + registers[line_data[3]] + line_data[5:11]

    elif (line_data[0] in b_type_instructions):
        line_data[3] = bin(int(line_data[3]))
        line_data[3] = line_data[3][2:]
        binary_output += b_type_encoding[line_data[0]]["opcode"] + line_data[3][10] + line_data[3][0:4] + b_type_encoding[line_data[0]]["funct3"] + registers[line_data[1]] + registers[line_data[2]] + line_data[3][4:10] + line_data[3][11]

    elif (line_data[0] in u_type_instructions):
        line_data[2] = bin(int(line_data[2]))
        line_data[2] = line_data[2][2:]
        binary_output += u_type_encoding[line_data[0]]["opcode"] + registers[line_data[1]] + line_data[2]

    elif (line_data[0] in j_type_instructions):
        line_data[2] = bin(int(line_data[2]))
        line_data[2] = line_data[2][2:]
        binary_output += j_type_encoding["jal"]["opcode"] + registers[line_data[1]] + line_data[2][11:19] + line_data[2][10] + line_data[2][0:9] + line_data[2][19]

    binary_output += '\n'
    l += 1

output_file = open("stdout.txt", "w")
output_file.write(binary_output)
output_file.close()