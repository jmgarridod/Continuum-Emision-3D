import numpy     as np
import constants as cons

#Fargo Outputs
time          = 2000	       #[snapshot]
model         = "Feedback3D_model1"
output_folder = "/home/jmgarrido/Simulaciones/Out/"+str(model)


#Dust
small_dust_size = 1e-5			#[cm]
dtg_ratio       = 1e-2


#Wavelengts
lam_min = 0.05	#[microns]
lam_max = 10000	#[microns]
nlam    = 200


#Photons
n_photon_therm      = 100000
n_photon_scat       = 10000
scattering_mode_max = 1

#1 Isotropic Scattering
#2 Anisotropic Scattering using Henyey-Greenstein               #No testeado
#3 Anisotropic Scattering using Tabulated Phase Function        #No testeado
#4 Anisotropic Scattering with Polarization for Last Scattering #No testeado
#5 Anisotropic Scattering with Polarization, Full Treatment     #No testeado


#Star
R0     = 1.0*cons.au			#[cm]
rstar  = 1.0*cons.rs			#[cm]
mstar  = 1.0*cons.ms			#[gr]
tstar  = 5777					#[K]
pstar  = np.array([0.,0.,0.])	#[cm],[cm],[cm]


# Image
wav        = 1.25e3  #[micron] #CRVAL3
incl       = 45      #Inclination
posang     = 0.0     #Position Angle
phi        = 0.0     #Azimuthal Rotation
npix       = 200     #
setthreads = 1       #
sizeau     = 0       #[au] Total size of the image, 0 for automatic size
stokes     = False   #
