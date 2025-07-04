import numpy as np

# Parámetros del cuadrotor
l = 0.1  # distancia del centro al motor (m)
d = 0.01  # constante de torque por drag

# Matriz F
F = np.array([
    [ 0,  l,   0,  -l],   # tau_x
    [-l,  0,   l,   0],   # tau_y
    [ d, -d,   d,  -d],   # tau_z
    [ 1,  1,   1,   1]    # T (empuje total)
])

# Pseudo-inversa de F (mínima norma cuadrática)
F_pinv = np.linalg.pinv(F)

# Supongamos un comando de control deseado:
# Estabilización con algo de empuje hacia abajo
u = np.array([0.0, 0.0, 0.0, 9.8])  # [tau_x, tau_y, tau_z, T]

# Calculamos las fuerzas necesarias por motor
fuerzas = F_pinv @ u

print("Fuerzas de los motores:")
for i, f in enumerate(fuerzas, start=1):
    print(f"Motor {i}: {f:.3f} N")
