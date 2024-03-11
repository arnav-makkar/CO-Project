import assembler as ac

def suggestions_for(instruction):

    all_instructions = ac.all_instructions

    def count(i):
        cnt = 0

        for x in instruction:
            if(x in i):
                cnt += 1
        return cnt

    relevant_instructions = filter(lambda x: count(x)>len(x)-1, all_instructions)
    # all the instructions which differ by just one character are included in the relevant instructions list

    print(f"'{instruction}' did not match any known instructions. Did you mean any of these? ") 
    print(*relevant_instructions, sep = ", ")