import math

T = 523.15  
P = 10.0
R = 0.08206
Tc = 407.5
Pc = 111.3 

tolerance = 1e-8
a = (27 * R**2 * Tc**2) / (64 * Pc)  
b = (R * Tc) / (8 * Pc)

lowerBound = 0.1
upperBound = 10.0

def bisectionMethod(T, P, a, b, R, lowerBound, upperBound):
    fLower = vanDerWaals(lowerBound, T, P, a, b, R) 
    fUpper = vanDerWaals(upperBound, T, P, a, b, R)
    
    count = 0
    if fLower * fUpper >= 0:
        return -1, count  

    while True:
        mid = (lowerBound + upperBound) / 2.0
        fMid = vanDerWaals(mid, T, P, a, b, R) 
        
        count += 1
        if abs(fMid) < tolerance:
            return mid, count
        
        if fMid * fLower < 0:
            upperBound = mid  
        else:
            lowerBound = mid
            
def vanDerWaals(v, T, P, a, b, R):
    return v**3 - ((b / P) + (R * T / P)) * v**2 + (a / P) * v - (a * b / P)

v_bisection, count_bisection = bisectionMethod(T, P, a, b, R, lowerBound, upperBound)

if v_bisection != -1:
    print("Bisection Method:")
    print(f"Molar volume: {v_bisection:.3f} L/mol.")
    print(f"Number of iterations: {count_bisection}")
else: 
    print("Bisection Method did not converge.")