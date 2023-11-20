import pprint

class Physics_Constant():
    """
    Record physics constant for the simulations
    """
    def __init__(self):
        # commonly used constants
        self.kB = 1.28064e-23  #  Boltzmann constant [J]
        self.T0 = 298.15  #  Room Temperature [K], 25 Celsius
        self.h = 6.62607e-34  # Planck constant [J/s]
        self.hbar = 1.05457e-34  # reduced Planck constant [J/s]
        self.G = 6.67430e-11  # Gravity constant [N*m^2*kg^{-2}]
        self.g = 9.81  # The acceleration of gravity [m/s^2]
        self.mu_B =  9.27401e-24  # Bohr magneton [J/T]
        self.e = 1.60217e-19 # elementary charge [C]
        self.c = 299792458  # the speed of light in vacuum [m/s]

        # density of materials
        self.rho_silica = 2e3  # density of silica [kg/m^3]
        self.rho_diamond = 3.5e3  # density of diamond [kg/m^3]
        
        # refractive index
        # self.silica = 

if __name__ == "__main__":
    constant = Physics_Constant()
    pprint.pprint(constant.__dict__)

