import math
from tabulate import tabulate

def g1A(x, y):
    return (10 - x**2) / y if y != 0 else float('inf')

def g2B(x, y):
    val = (57 - y) / (3 * x) if x != 0 else float('inf')
    return math.sqrt(val) if val >= 0 else float('nan')

def jacobi_iteration_fixed(x0, y0, epsilon, max_iter=20):
    x, y = x0, y0
    history = [[0, x, y, 0, 0]]
    converged = False

    for i in range(1, max_iter + 1):
        x_old, y_old = x, y
        
        x_new = g1A(x_old, y_old)
        y_new = g2B(x_old, y_old)

        if math.isnan(x_new) or math.isnan(y_new) or math.isinf(x_new) or math.isinf(y_new):
            print("💥 Solusi divergen atau menghasilkan nilai tidak valid.")
            break
        
        delta_x = abs(x_new - x_old)
        delta_y = abs(y_new - y_old)
        
        x, y = x_new, y_new
        history.append([i, x, y, delta_x, delta_y])

        if delta_x < epsilon and delta_y < epsilon:
            converged = True
            print("✨ Konvergensi tercapai.")
            break
    
    if not converged and i >= max_iter:
        print("⚠️ Iterasi maksimum tercapai, solusi divergen.")

    print(tabulate(history, headers=["Iterasi (r)", "x", "y", "deltaX", "deltaY"], floatfmt=".6f"))

print("--- Metode Iterasi Titik-Tetap (Jacobi) ---")
jacobi_iteration_fixed(1.5, 3.5, 0.000001)