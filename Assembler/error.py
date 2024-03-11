import assembler_code as ps

def suggestions_for(instruction):
    all_instructions = [
        *ps.R_Type_Instructions,
        *ps.I_Type_Instructions,
        *ps.S_Type_Instructions,
        *ps.B_Type_Instructions,
        *ps.U_Type_Instructions,
        *ps.J_Type_Instructions,
        *ps.Bonus
    ]

    matches = [(i, sum(1 for x in instruction if x in i)) for i in all_instructions]
    matches.sort(key=lambda x: x[1], reverse=True)

    suggested_instructions = [ins for ins, count in matches if count > len(ins) - 2]

    print(f"{instruction} did not match any known instruction, perhaps you meant:") 
    print(*suggested_instructions, sep=", ")

suggestions_for(instruction)