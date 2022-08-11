Steps to make line radiative transfer images:


0) Edit: parameters.py      
1) Run : make
2) Run : python3 set_main.py 
3) Run : radmc3d mctherm setthreads x
3) Run : python3 set_images.py
4) Run : python3 plot_images.py
5) Run : python3 save_fits.py


Porque es importante hacer make antes que todo:

El objetivo es calcular la temperatura de los granos de polvo a traves de la simulacion de Monte-Carlo (radmc3d mctherm).
Esto parte por tener el tamano de los granos, en este caso 1e-5 cm o 0.1 microns.
Su distribucion de densidad en el disco viene por una porcion del gas, a travez del dust-to-gas ratio.

El tratamiento puede considera scattering para ser mas realista.
En este caso los parametros de la opcidad estaran para cada specie de polvo (1 en este caso), que sera un archivo
llamado "dustkapscatmat_1e-01.inp". Para crear este archivo se llama a la funcion: "create_dustkapscatmat_file" que
esta dentro del archivo "makedustopacfortran.py" utilizando una espcie de silicates llamado descrito en "olivine.lnk". 
El script utilizara una programa que se creara a partir de la rutina
en fortran. Esta es "make_scatmat_smoothed.f90" que utilizara "bhmie.f" para generar el ejecutable "make_smoothed" que sera
llamado por "create_dustkapscatmat_file", como se menciono anteriormente.
Por ello es muy importante crear este ejecutable haciendo un "make" antes de correr "set_main.py", de otro modo no se crearan 
las opacidades para el polvo y lanzara un error.



