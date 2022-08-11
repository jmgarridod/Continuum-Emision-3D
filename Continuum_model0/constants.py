#Constants

rs  = 6.96e10        # Solar radius            [cm]
ms  = 1.98892e33     # Solar mass              [gr]
au  = 1.49598e13     # Astronomical Unit       [cm]
G   = 6.67408e-08    # Gravitational constant  [cm^3/g/s^2]
kb  = 1.3807e-16     # Bolzmann's constant     [erg/K]
mp  = 1.6726e-24     # Mass of proton          [gr]
mu  = 2.35           #                         [gr/mol]
pc  = 3.086e+18      # Parsec                  [cm]
c   = 2.99792e10     # Speed of the light      [cm/s]
eV  = 1.60218e-12    # Electron Volt           [erg]
Rg  = 8.314472e7     # Gas constat             [erg/K/mol]


u_density     = ms/au**2             # Surface Denisty   [gr/cm/cm]
u_density_vol = ms/au**3             # Volume Denisty    [gr/cm/cm/cm]
u_time        = (au**3/G/ms)**(0.5)  # Time              [sec]
u_velocity    = au/u_time            # Velocity          [cm/s]
u_energy_vol  = ms/(u_time)**2/au    # Volume energy     [erg/cm/cm/cm]


