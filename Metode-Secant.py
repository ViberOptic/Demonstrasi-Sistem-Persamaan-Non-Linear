import math
from tabulate import tabulate

def u(x, y):
    return x**2 + x*y - 10

def v(x, y):
    return y + 3*x*y**2 - 57

def secant_method(x0, y0, epsilon, max_iter=100):
    x, y = x0, y0
    h = 1e-6
    history = []
    
    for i in range(max_iter):
        delta_x = float('inf')
        delta_y = float('inf')

        if i > 0:
            delta_x = abs(x - history[-1][1])
            delta_y = abs(y - history[-1][2])
            
        history.append([i, x, y, delta_x if i > 0 else 0, delta_y if i > 0 else 0])
        
        if i > 0 and (delta_x < epsilon and delta_y < epsilon):
            print("✨ Konvergensi tercapai.")
            break
        
        u_val = u(x, y)
        v_val = v(x, y)
        
        du_dx_approx = (u(x + h, y) - u_val) / h
        du_dy_approx = (u(x, y + h) - u_val) / h
        dv_dx_approx = (v(x + h, y) - v_val) / h
        dv_dy_approx = (v(x, y + h) - v_val) / h
        
        det = du_dx_approx * dv_dy_approx - du_dy_approx * dv_dx_approx
        if det == 0:
            print("💥 Determinan Jacobi nol, metode gagal.")
            break
            
        x_new = x - (u_val * dv_dy_approx - v_val * du_dy_approx) / det
        y_new = y - (v_val * du_dx_approx - u_val * dv_dx_approx) / det
        
        x, y = x_new, y_new
    else:
        print("⚠️ Iterasi maksimum tercapai, solusi mungkin tidak konvergen.")
        
    print(tabulate(history, headers=["Iterasi (r)", "x", "y", "deltaX", "deltaY"], floatfmt=".6f"))

print("\n--- Metode Secant (Finite-Difference Newton) ---")
secant_method(1.5, 3.5, 0.000001)