import numpy as np

# functions for taylor gravity
def y_with_friction(t, y0, v0, g, gamma):
    return y0 - (g / gamma) * t - (1 / gamma) * (v0 + g / gamma) * (np.exp(-gamma * t) - 1)

def y_without_friction(t, y0, v0, g):
    return y0 + v0 * t - 0.5 * g * t**2

def y_taylor(t, y0, v0, g, gamma):
    return y0 + v0 * t - 0.5 * (g + gamma * v0) * t**2