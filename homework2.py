'''
Amira Johnson
Problem #4 -- Homework 2
'''

import math 
def intensity(A, x, y, sigma_squared):
    M, N = len(A), len(A[0])
    top_value = 0
    bottom_value = 0

    for p in range(1, M):
        for q in range(1, N): 
            top_value += A[p][q] * math.e**(((-1*sigma_squared)*((x-p)**2 + (y-q)**2)))
            bottom_value += math.e ** (((-1*25)*((x-p)**2 + (y-q)**2)))
    
    return top_value / bottom_value

#calculate gradient
def f(A, T, x, y, sigma_squared):
    result = 0
    m, n = len(T), len(T[0]) 
    for i in range(1, m):
        for j in range(1, n):
            result += (T[i][j] - intensity(A, i+x, j+y, sigma_squared))**2
    return result


def do_optimization(A, T, x, y, deltax, deltay, dx, dy):

    f_xx = f(A, T, x + deltax, y) - 2*f(A, T, x + deltax, y) + f(A, T, x-deltax, y) / deltax ** 2

    f_yy = f(A, T, x, y + deltay) - 2*f(A, T, x, y + deltay) + f(A, T, x, y-deltay) / deltay ** 2
    
    f_xy = f(A, T, x + deltax, y + deltay) - 2*f(A, T, x+deltax, y + deltay) + f(A, T, x-deltax, y-deltay) / deltay ** 2

    x+=dx
    y+=dy

    return x, y

def pseudo_global_optimizer(A, T, deltax, deltay, M, N, sigma_squared):
    best_pair, minimal = (-1, -1), 0
    for x in range(1, M-m):
        for y in range(1, N-n):
            result = f(A, T, x, y, sigma_squared)
            if result < minimal:
                minimal = result
                best_pair = (x, y)
            y+=deltay
        x+=deltax
    return best_pair


inputs = open("PS2 test 1.txt", "rt").read()
inputs = inputs.split('\n')

parameters = inputs[0]
MN_vals = inputs[1].split(" ")
M, N = int(MN_vals[0]), int(MN_vals[1])
deltax, deltay, dx, dy, sigma_squared = parameters.split(" ")
deltax = float(deltax)
deltay = float(deltay)
dx = float(dx)
dy = float(dy)
sigma_squared = int(sigma_squared)

fake_A = inputs[2:M+2]
A = []

for row in fake_A:
    new = []
    for val in row.split(" "):
        if val != '':
            new.append(float(val))
    A.append(new)


m, n = inputs[M+2].split(" ")
m, n = int(m), int(n)

T = []
fake_T = inputs[M+3:]

for row in fake_T:
    new = []
    for val in row.split(" "):
        if val != '':
            new.append(float(val))
    T.append(new)


print(pseudo_global_optimizer(A, T, deltax, deltay, M, N, sigma_squared))

