import re
from data import R_Type, I_Type, S_Type, B_Type, U_Type, J_Type, Registers
import suggester as sg

R_Type_Instructions = ["add", "sub", "slt", "sltu", "xor", "sll", "srl", "or", "and"]
I_Type_Instructions = ["lb", "lh", "lw", "ld", "addi", "sltiu", "jalr"]
S_Type_Instructions = ["sb", "sh", "sw", "sd"]
B_Type_Instructions = ["beq", "bne", "bge", "bgeu", "blt", "bltu"]
U_Type_Instructions = ["auipc", "lui"]
J_Type_Instructions = ["jal"]
Bonus = ["mul", "rst", "halt", "rvrs"]
Unique_Registers = ["zero", "ra", "sp", "gp", "tp", "t0", "t1", "t2", "s0", "fp", "s1", "a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "s11", "t3", "t4", "t5", "t6"]

