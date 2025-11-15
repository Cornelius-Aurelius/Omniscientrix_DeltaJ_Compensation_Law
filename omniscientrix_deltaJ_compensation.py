# Omniscientrix δJ-Equilibrium Compensation Law Verification
# ASCII-safe simulation of delta-J relaxation toward equilibrium.

import numpy as np

# domain
N = 400
L = 1.0
x = np.linspace(0, L, N, endpoint=False)
dx = x[1]-x[0]

# initial informational field
p = np.sin(4*np.pi*x) + 1.2
p = p + 1e-6
p = p / (np.sum(p)*dx)

# delta-J functional (discrete gradient)
def deltaJ(f):
    g = (np.roll(f,-1) - np.roll(f,1)) / (2*dx)
    return np.sum(np.abs(g)) * dx

# relaxation evolution
def evolve(f):
    lap = (np.roll(f,-1) - 2*f + np.roll(f,1)) / dx**2
    return f + 0.00008 * lap

history = []

for _ in range(500):
    history.append(deltaJ(p))
    p = evolve(p)
    p = np.clip(p, 1e-12, None)
    p = p / (np.sum(p)*dx)
