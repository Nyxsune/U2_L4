"""
Connor Cox
U2 Lab4
MAtrix Arithmetic
"""


def mat_sum(m1, m2):
    x1 = len(m1[0])
    y1 = len(m1)
    x2 = len(m2[0])
    y2 = len(m2)
    
    if x1 == x2 and y1 == y2:
        new = [[0]*x1 for i in range(y1)]
        for i in range(x2):
            for j in range(y2):
                new[i][j] = m1[i][j] + m2[i][j]
        solution = new
    else:
        solution = "no solution"

    return solution


def mat_mul(m1, m2):
    x1 = len(m1[0])
    y1 = len(m1)
    x2 = len(m2[0])
    y2 = len(m2)
    
    if x1 == y2:
        new = [[0]*x2 for i in range(y1)]

        

        solution = new
    else:
        solution = "no solution"

    return solution