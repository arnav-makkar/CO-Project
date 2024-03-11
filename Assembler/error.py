import assembler_code as ps

def suggestions_for(instruction):
    all_instructions = ps.R_Type_Instructions + ps.I_Type_Instructions + ps.S_Type_Instructions + ps.B_Type_Instructions + ps.U_Type_Instructions + ps.J_Type_Instructions + ps.Bonus

    def suggester(instruction):
        def count_matches(i):
            return sum(1 for x in instruction if x in i)
        return count_matches

    suggester_function = suggester(instruction)
    sorted_instructions = sorted(all_instructions, key=suggester_function, reverse=True)
    suggested_instructions = [i for i in sorted_instructions if suggester_function(i) > len(i) - 2]

    print(f"{instruction} did not match any known instruction, perhaps you meant") 
    print(*suggested_instructions, sep=", ")

