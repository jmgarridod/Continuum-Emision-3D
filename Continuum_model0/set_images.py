import os
import parameters as par

command  = "radmc3d image"+" "

command += "npix"       +" "+ str(par.npix)       +" "
command += "incl"       +" "+ str(par.incl)       +" "
command += "posang"     +" "+ str(par.posang)     +" "
command += "phi"        +" "+ str(par.phi)        +" "
command += "lambda"     +" "+ str(par.wav)        +" "
command += "setthreads" +" "+ str(par.setthreads) +" "

if par.sizeau !=0:
	command += "sizeau" +" "+ str(par.sizeau) +" "

if par.stokes == True:
	command += "stokes" +" "
	
print(command) 
os.system(command)

