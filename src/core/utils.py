def space_between(input:str, nbr:int) -> str:
    res = ""

    for i in range(len(input)):
        if i % (nbr) == 0:
            res += ' '

        res += input[i]

    return res