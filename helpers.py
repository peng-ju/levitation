import numpy as np
from physics_constant import Physics_Constant


Constant = Physics_Constant()


def cal_mass_sphere(radius: float, rho: float) -> float:
    """
    calculate the mass of a sphere

    :param radius: radius of the sphere
    :param rho: density of the meterail
    :return M: calculated mass of the sphere
    """
    M = rho * 4/3 * np.pi * radius**2

    return M


def cal_mass_dumbbell(radius: float, rho: float) -> float:
    """
    calculate the mass of a dumbbell composed of two spheres

    :param radius: radius of radius of a single sphere
    :param rho: density of the meterail
    :return M: calculated mass of the dumbbell
    """
    M = 2 * cal_mass_sphere(radius, rho)

    return M


def cal_I_sphere(radius: float, rho: float) -> float:
    """
    calculate the moment of inertia of a sphere

    :param radius: radius of the sphere
    :param rho: density of the meterail
    :return I: calculated moment of inertia of the sphere
    """
    I = 2/5 * np.pi * cal_mass_sphere(radius, rho) * radius**2

    return I


def cal_I_dumbbell(radius: float, rho: float) -> float:
    """
    calculate the moment of inertia of a dumbbell composed of two spheres

    :param radius: radius of a single sphere
    :param rho: density of the meterail
    :return I: calculated moment of inertia of the dumbbell
    """
    I = 14/5 * np.pi * cal_mass_sphere(radius, rho) * radius**2

    return I


def cal_mean_free_path(pressure: float) -> float:
    """
    calculate the mean free path of the air molecules

    :param pressure: pressure of the vacuum
    :return mean_free_path: calculated mean free path
    """
    mean_free_path = 67e-9 * 760 / pressure # mean free path of air molecules at pressure [m]

    return mean_free_path


def cal_Gamma_COM_sphere(pressure: float, radius: float, rho: float) -> float:
    """
    calculate COM motion damping of a sphere due to residual gas in vacuum.

    :param pressure: pressure of the vacuum
    :param radius: radius of the sphere
    :param rho: density of the meterail
    :return Gamma: calculated COM motion damping of a sphere
    """
    viscosity_air = Constant.eta_air
    mean_free_path = cal_mean_free_path(pressure)
    Kn = mean_free_path / radius  # Knedsen number
    c_K = 0.31 * Kn / (0.785 + 1.152 * Kn + Kn**2) 
    Gamma = (6 * np.pi * viscosity_air * radius / cal_mass_sphere(radius, rho)) * (0.619 / (0.619 + Kn)) * (1 + c_K)

    return Gamma