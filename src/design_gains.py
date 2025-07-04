import numpy as np
from scipy.signal import place_poles

# ============================================
# Diseno del Observador y Controlador del Quadrotor
# ============================================

# Sistema de orientación: A y C
A = np.zeros((6, 6))
A[:3, 3:] = np.eye(3)  # φ' = p, θ' = q, ψ' = r
C = np.array([
    [1, 0, 0, 0, 0, 0],  # Se mide φ
    [0, 1, 0, 0, 0, 0],  # Se mide θ
    [0, 0, 1, 0, 0, 0]   # Se mide ψ
])

# ============================================
# Diseño del observador (ganancia L)
# ============================================

# Polos deseados del observador (rápidos para buena convergencia)
observer_poles = [-6, -6, -6, -8, -8, -8]

# Cálculo de la ganancia L mediante colocación de polos
L_result = place_poles(A.T, C.T, observer_poles)
L = L_result.gain_matrix.T

print("Ganancia del observador (L):")
print(L)

# ============================================
# Diseño del controlador (ganancia K)
# ============================================

# Redefinir A para que no esté sobreescrito por zeros
A = np.array([
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
])

# Matriz B del sistema (torques)
B = np.array([
    [0,   0,   0],
    [0,   0,   0],
    [0,   0,   0],
    [100, 0,   0],
    [0, 100,   0],
    [0,   0,  50]
])

# Polos deseados del sistema en lazo cerrado
controller_poles = [-3, -3, -3, -4, -4, -4]

# Cálculo de la ganancia K mediante colocación de polos
K = place_poles(A, B, controller_poles).gain_matrix

print("\n Ganancia del controlador (K):")
print(K)