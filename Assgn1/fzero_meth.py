import time
from scipy.optimize import fsolve

start = time.time()

T = 523.15   # Temperature in K 
P = 10       # Pressure in atm
Tc = 407.6   # Critical temperature
Pc = 111.3   # Critical Pressure  
R = 0.082    # Gas constant

a = (27 * R**2 * Tc**2) / (64 * Pc)
b = (R * Tc) / (8 * Pc)

# Van der Waals equation
def equation(v):
    return (P + a / v**2) * (v - b) - R*T

# Initial guess
v0 = 4  

# Find root using fsolve
v_fsolve = fsolve(equation, v0)[0]   

print(f"fsolve Result : v = {v_fsolve:.3f}")

end = time.time()
elapsed = end - start
print(f"Runtime = {elapsed:.3f} seconds")