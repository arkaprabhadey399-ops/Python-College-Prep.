import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Enable clean math layout printing in your terminal window
sp.init_printing(use_unicode=True)

print("--- 1. CALCULUS CALCULATOR ---")
x = sp.Symbol('x')
# Finds the exact symbolic integral of x^2 * sin(x)
integral = sp.integrate(x**2 * sp.sin(x), x)
print("Integral result:")
sp.pprint(integral)

print("\n--- 2. MATRIX & COMPLEX MATH ---")
# Create a matrix with complex numbers (use 'j' for imaginary units)
mat = np.array([[1 + 2j, 3], 
                [4, 5 - 1j]])
print("Matrix Inverse:\n", np.linalg.inv(mat))

print("\n--- 3. GRAPH GENERATOR ---")
# Setup data for a 3D calculus wave
x_arr = np.linspace(-5, 5, 100)
y_arr = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x_arr, y_arr)
Z = np.sin(X) * np.cos(Y)

fig = plt.figure(figsize=(7, 5))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='coolwarm')
ax.set_title("3D Function Plot")

print("Opening your interactive 3D graph...")
plt.show()
