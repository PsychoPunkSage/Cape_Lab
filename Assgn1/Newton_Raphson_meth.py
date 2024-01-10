# start = time.time()
T = 523.15   # Temperature in K
P = 10       # Pressure in atm
Tc = 407.6   # Critical temperature 
Pc = 111.3   # Critical Pressure
R = 0.082    # Gas constant

a = (27 * R**2 * Tc**2) / (64 * Pc)
b = (R * Tc) / (8 * Pc)

# Initial guess
v_guess = 4 

for i in range(50):
    f = (P + a / v_guess**2) * (v_guess - b) - R * T
    f_prime = -2 * a / v_guess**3 + P + b / v_guess**2
    
    v_next = v_guess - f/f_prime
    
    if abs(v_next - v_guess) < 1e-6:
        break
    
    v_guess = v_next

print(f"Newton Raphson Iteration Result : v = {v_next:.3f}, iterations = {i+1}")
# print(f"Runtime = {elapsed:.3f} seconds")