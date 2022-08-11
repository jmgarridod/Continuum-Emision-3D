import os
import sys
import shutil

model_in  = "0"
model_out = "1"

disk_name = "Continuum"

folder = "/home/jmgarrido/RADMC3D/ContinuumEmission3D/"
data1  = str(folder)+str(disk_name)+"_model"+str(model_in)
data2  = str(folder)+str(disk_name)+"_model"+str(model_out)


sys.path.insert(0,data1)

files_copy = ["Makefile",
              "bhmie.f",
              "make_scatmat_smoothed.f90",
              "makedustopacfortran.py",
              "olivine.lnk",
              "constants.py",
              "parameters.py",
              "plot_images.py",
              "save_fits.py",
              "set_images.py",
              "set_write.py",
              "set_main.py",
              "README.txt"]

try:
	os.mkdir(data2)
	
	print(data1,"to",data2)
	for files in files_copy:
		shutil.copy(data1+"/"+str(files),data2+"/"+str(files))
		print(files)

except:
	print("La carpeta ya existe")
	print("No se sobre-escribio ningun archivo")




