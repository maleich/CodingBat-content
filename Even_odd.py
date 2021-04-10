#By Jacob '24
def even_and_odd(str): 
    count = 0
    first_str = ''
    second_str = ''
    final_str = ''
    for letter in str:
        if count %2 == 0:
            first_str += letter
            count += 1
        else:
            second_str += letter
            count += 1
    final_str = first_str + second_str
    return final_str
