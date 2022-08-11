#----------------------------------------------------------------------#
# Write the wavelength_micron.inp file
#----------------------------------------------------------------------#
def write_wavelength_micron(nlam,lam):
	print("Writing: wavelength_micron.inp","\n")
	with open('wavelength_micron.inp','w+') as f:
		f.write('%d\n'%(nlam))
		for value in lam:
			f.write('%13.6e\n'%(value))
		f.close()


#----------------------------------------------------------------------#
# Write the stars.inp file
#----------------------------------------------------------------------#
def write_stars(nlam,lam,rstar,mstar,pstar_0,pstar_1,pstar_2,tstar):
	print("Writing: stars.inp","\n")
	with open('stars.inp','w+') as f:
		f.write('2\n')
		f.write('1 %d\n'%(nlam))
		f.write('%13.6e %13.6e %13.6e %13.6e %13.6e\n'%(rstar,mstar,pstar_0,pstar_1,pstar_2))
		for value in lam:
			f.write('%13.6e\n'%(value))
		f.write('\n%13.6e\n'%(-tstar))
		f.close()


#----------------------------------------------------------------------#
# Write the amr_grid.inp file
#----------------------------------------------------------------------#
def write_amr_grid(nr,ntheta,nphi,r,theta,phi):
	print("Writing: amr_grid.inp","\n")
	with open('amr_grid.inp','w+') as f:
		f.write('1\n')                         # iformat
		f.write('0\n')                         # AMR grid style  (0=regular grid, no AMR)
		f.write('100\n')                       # Coordinate system: spherical
		f.write('0\n')                         # gridinfo
		f.write('1 1 1\n')                     # Include r,theta,phi coordinates
		f.write('%d %d %d\n'%(nr,ntheta,nphi)) # Size of grid
		for value in r:
			f.write('%13.6e\n'%(value))      # X coordinates (cell walls)
		for value in theta:
			f.write('%13.6e\n'%(value))     # Y coordinates (cell walls) (use higher precision here)
		for value in phi:
			f.write('%13.6e\n'%(value))      # Z coordinates (cell walls)
		f.close()

#----------------------------------------------------------------------#
# Write the radmc3d.inp control file
#----------------------------------------------------------------------#
def write_radmc3d(n_photon_therm,n_photon_scat,scattering_mode_max):
	print("Writing: radmc3d.inp","\n")
	with open('radmc3d.inp','w+') as f:
		f.write('nphot_therm = %d\n'%(n_photon_therm))
		f.write('nphot_scat = %d\n'%(n_photon_scat))
		f.write('scattering_mode_max = %d\n'%(scattering_mode_max))
		f.write('iranfreqmode = 1\n')
		f.close()


#----------------------------------------------------------------------#
#//////////////////////////////////////////////////////////////////////#
#----------------------------------------------------------------------#


#----------------------------------------------------------------------#
# Write the dustopac.inp file
#----------------------------------------------------------------------#
def write_dustopac(nspec,dust_sizes_microns):
	print("Writing: dustopac.inp","\n")
	with open('dustopac.inp','w+') as f:
		f.write('2               Format number of this file\n')
		f.write('{}               Nr of dust species\n'.format(nspec))
		f.write('============================================================================\n')
		for dust_size_microns_i in dust_sizes_microns:
			f.write('10              Way in which this dust species is read\n')
			f.write('0               0=Thermal grain\n')
			f.write(('{0:'+"8.2e"+'}        Extension of name of dustkapscatmat_***.inp file\n').format(dust_size_microns_i))
			f.write('----------------------------------------------------------------------------\n')
		f.close()
		
#----------------------------------------------------------------------#
# Write the gas temperature
#----------------------------------------------------------------------#
def write_gas_temperature(nr,ntheta,nphi,temp):
	print("Writing: gas_temperature.inp","\n")
	with open('gas_temperature.inp','w+') as f:	
		f.write('1\n')                       # Format number
		f.write('%d\n'%(nr*ntheta*nphi))     # Nr of cells
		for phi_i in range(nphi):
			for theta_i in range(ntheta):
				for r_i in range(nr):
					f.write(str(temp[theta_i,theta_i,phi_i])+' \n')
		f.close()

#----------------------------------------------------------------------#
# Write the dust density
#----------------------------------------------------------------------#
def write_dust_density(nr,ntheta,nphi,nspec,rho_dust):
	with open('dust_density.inp','w+') as f:
		print("Writing: dust_density.inp")
		f.write('1\n')                       # Format number
		f.write('%d\n'%(nr*ntheta*nphi))     # Nr of cells
		f.write('{}\n'.format(nspec))        # Nr of dust species
		for phi_i in range(nphi):
			for theta_i in range(ntheta):
				for r_i in range(nr):
					f.write(str(rho_dust[theta_i,r_i,phi_i])+' \n')
	f.close()
