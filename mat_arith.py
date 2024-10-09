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
    l1 = len(m1[0])
    h1 = len(m1)
    l2 = len(m2[0])
    h2 = len(m2)
    print(h1, l1, h2, l2)
    
    if l1 == h2:
        new = [[0]*l2 for i in range(h1)]
        for i in range(h1):
            for j in range(l2):
                for z in range(l1):
                    new[i][j] += m1[i][z] * m2[z][j]

        solution = new
    else:
        solution = "no solution"

    return solution