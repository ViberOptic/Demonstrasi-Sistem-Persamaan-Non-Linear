import math
from tabulate import tabulate

def u(x, y):
    return x**2 + x*y - 10

def v(x, y):
    return y + 3*x*y**2 - 57

def du_dx(x, y): return 2*x + y
def du_dy(x, y): return x
def dv_dx(x, y): return 3*y**2
def dv_dy(x, y): return 1 + 6*x*y

def newton_raphson(x0, y0, epsilon, max_iter=100):
    x, y = x0, y0
    history = []
    
    for i in range(max_iter):
        u_val = u(x,y)
        v_val = v(x,y)
        
        delta_x = float('inf')
        delta_y = float('inf')
        
        if i > 0:
            delta_x = abs(x - history[-1][1])
            delta_y = abs(y - history[-1][2])

        history.append([i, x, y, delta_x if i > 0 else 0, delta_y if i > 0 else 0])
        
        if i > 0 and (delta_x < epsilon and delta_y < epsilon):
            print("✨ Konvergensi tercapai.")
            break
        
        det = du_dx(x,y) * dv_dy(x,y) - du_dy(x,y) * dv_dx(x,y)
        if det == 0:
            print("💥 Determinan Jacobi nol, metode gagal.")
            break
        
        x_new = x - (u_val * dv_dy(x,y) - v_val * du_dy(x,y)) / det
        y_new = y - (v_val * du_dx(x,y) - u_val * dv_dx(x,y)) / det
        
        x, y = x_new, y_new
    else:
        print("⚠️ Iterasi maksimum tercapai, solusi mungkin tidak konvergen.")

    print(tabulate(history, headers=["Iterasi (r)", "x", "y", "deltaX", "deltaY"], floatfmt=".6f"))

print("\n--- Metode Newton-Raphson ---")
newton_raphson(1.5, 3.5, 0.000001)