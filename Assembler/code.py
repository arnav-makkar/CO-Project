import re
from data import *

r_type_instructions = ["add", "sub", "slt", "sltu", "xor", "sll", "srl", "or", "and"]
i_type_instructions = ["lb", "lh", "lw", "ld", "addi", "sltiu", "jalr"]
s_type_instructions = ["sb", "sh", "sw", "sd"]
b_type_instructions = ["beq", "bne", "bge", "bgeu", "blt", "bltu"]
u_type_instructions = ["auipc", "lui"]
j_type_instructions = ["jal"]
bonus = ["mul", "rst", "halt", "rvrs"]
unique_registers = ["zero", "ra", "sp", "gp", "tp", "t0", "t1", "t2", "s0", "fp", "s1", "a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "s11", "t3", "t4", "t5", "t6"]

