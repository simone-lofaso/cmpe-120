def decToBinary(num):
    solution = ""
    while (num >= 1):
        solution = str(num % 2) + solution
        num = num // 2
    return solution