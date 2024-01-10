import math

T = 523.15 
P = 10.0
R = 0.08206
Tc = 407.5
Pc = 111.3
maxIterations = 1000
tolerance = 1e-8
a = (27 * R * R * Tc * Tc) / (64 * Pc)
b = (R * Tc) / (8 * Pc)  
initialGuess = R * T / P

def fixedPointIteration(T, P, a, b, R, initialGuess):
    v = initialGuess 
    count = 0
    while True:
        vNext = (R * T / (P + (a / v**2))) + b
        count += 1
        if abs(vNext - v) < tolerance:
            break  
        v = vNext
    return v, count

v_fp, count_fp = fixedPointIteration(T, P, a, b, R, initialGuess)

if v_fp != -1:
    print('Fixed-Point Iteration Method:')
    print(f'Molar volume: {v_fp:.3f} L/mol.') 
    print(f'Number of iterations: {count_fp}')
else:
    print('Fixed-Point Iteration did not converge.')