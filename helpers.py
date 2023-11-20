import numpy as np


def mass_sphere(radius, rho):
    M = rho * 4/3 * np.pi * radius**2

    return M


def mass_dumbbell(radius, rho):
    M = 2 * mass_sphere(radius, rho)

    return M


def I_sphere(radius, rho):
    I = 2/5 * np.pi * mass_sphere(radius, rho) * radius**2

    return I


def I_dumbbell(radius, rho):
    I = 14/5 * np.pi * mass_sphere(radius, rho) * radius**2

    return I
