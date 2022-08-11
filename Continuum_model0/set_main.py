import os
import gc
import time
import numpy               as np
import matplotlib.pyplot   as plt
import parameters          as par
import constants           as cons
import set_write           as sw
import makedustopacfortran as mdof

start_time = time.time()


#----------------------------------------------------------------------#
# Get Folder and Time
#----------------------------------------------------------------------#
dir      = par.output_folder
snapshot = par.time


#----------------------------------------------------------------------#
# Call .par file
#----------------------------------------------------------------------#
def P(parametro):
	return valores_par[parametros_par.index(parametro)]
	
variables_par  = np.genfromtxt(dir+"/variables.par",dtype={'names': ("parametros","valores"),'formats': ("|S30","|S300")}).tolist()
parametros_par = []
valores_par    = []
for posicion in variables_par:
	parametros_par.append(posicion[0].decode("utf-8"))
	valores_par.append(posicion[1].decode("utf-8"))


#----------------------------------------------------------------------#
# Domain and Mesh
#----------------------------------------------------------------------#
nr     = int(P("NY"))
nphi   = int(P("NX"))
ntheta = int(P("NZ"))

#**********************************************************************#
#RADMC3D doesn't resolve azimuthal grids from phi_min to phi_max
#It's necessary that phi_min=0 and phi_max=2pi

#phi    = np.fromfile(dir+'/domain_x.dat',sep='\n')+np.pi
phi     = np.linspace(0.e0,np.pi*2.e0,nphi+1)
#**********************************************************************#

r      = np.fromfile(dir+'/domain_y.dat',sep='\n')[3:-3]
theta  = np.fromfile(dir+'/domain_z.dat',sep='\n')[3:-3]

r_c     = 0.5*(r[1:]      + r[:-1]    )
phi_c   = 0.5*(phi[1:]    + phi[:-1]  )
theta_c = 0.5*(theta[:-1] + theta[1:] )

print("nr  :",nr  ,"\t","r  :",len(r)  ,"\t","r_c  :",len(r_c)  )
print("nphi:",nphi,"\t","phi:",len(phi),"\t","phi_c:",len(phi_c))
print("ntheta:",ntheta,"\t","theta:",len(theta),"\t","theta_c:",len(theta_c),"\n")


#----------------------------------------------------------------------#
# Function to call Fields
#----------------------------------------------------------------------#
def Field(snapshot,field):
	F = np.fromfile(dir+"/"+"gas"+str(field)+str(snapshot)+".dat").reshape(ntheta,nr,nphi)
	return F


#----------------------------------------------------------------------#
# Write necessary files
#----------------------------------------------------------------------#
lam  = np.logspace(np.log10(par.lam_min),np.log10(par.lam_max),par.nlam) # [microns]
sw.write_wavelength_micron(par.nlam,lam)

sw.write_stars(par.nlam,lam,par.rstar,par.mstar,par.pstar[0],par.pstar[1],par.pstar[2],par.tstar)

sw.write_amr_grid(nr,ntheta,nphi,r*cons.au,theta,phi)

sw.write_radmc3d(par.n_photon_therm,par.n_photon_scat,par.scattering_mode_max)

#----------------------------------------------------------------------#
# Build Gas Temperature
#----------------------------------------------------------------------#
rho_gas  = Field(snapshot,"dens")*cons.u_density_vol      # [gr/cm/cm/cm]
energy   = Field(snapshot,"energy")*cons.u_energy_vol     # [erg/cm/cm/cm]
gamma    = float(P("GAMMA"))
temp_gas = energy/rho_gas/(cons.Rg/cons.mu)*(gamma-1)     # [K]

sw.write_gas_temperature(nr,ntheta,nphi,temp_gas)


#----------------------------------------------------------------------#
# Build Dust Temperature
#----------------------------------------------------------------------#
rho_dust           = rho_gas*par.dtg_ratio      # [gr/cm/cm/cm]
dust_sizes         = [par.small_dust_size]      # [cm]
nspec              = len(dust_sizes)
dust_sizes_microns = np.asarray(dust_sizes)*1e4 # [microns]

sw.write_dust_density(nr,ntheta,nphi,nspec,rho_dust)

#This function creates a file, which describes the opacities to be read.
#In this case, the file should be written something like that, "dustkapscatmat_(size in microns).inp".
sw.write_dustopac(nspec,dust_sizes_microns)

for dust_sizes_microns_i in dust_sizes_microns:
	name_dust_size = ('{0:'+"8.2e"+'}').format(dust_sizes_microns_i).strip()
	name_opac_file = 'dustkapscatmat_'+str(name_dust_size)+'.inp'
	string_dust_size = ("{0:"+"8.2"+"}").format(dust_sizes_microns_i)
	if(not os.path.isfile(name_opac_file)):
		print("Creating opacity for grain size "+str(string_dust_size)+" micron radius")
		mdof.create_dustkapscatmat_file(dust_sizes_microns_i,"olivine",
							   nsample=20,logawidth=0.05,errortol=1e99,
							   chopangle=5.,renametosize=True,sizeformat="8.2e",
							   command="./makeopac_smoothed",scatmat=True,kappa=False)
	else:
		print("Have been already created the opacity for grain size "+str(string_dust_size)+" micron radius")
print("\n")


print("--- %s seconds ---" % (time.time() - start_time))
