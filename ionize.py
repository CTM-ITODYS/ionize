
#
#    **********
#    * ionize *
#    **********
#
# purpose: provide the number of Na+ and Cl-
# ions to add in order to reach a defined concentration
#
# usage: python ionize.py global_charge number_of_water concentration(mM)
#
# example: python ionize.py -186 80000 150
#
# results of calculation are placed in the file ionize.results.txt
#
# =====> Import
#
import sys  # getting information from line arguments (here 1, 2 and 3)
#
# =====> Declaration
#
glob_charge=int(sys.argv[1])
num_wat=int(sys.argv[2])
concentration=float(sys.argv[3])
num_Na=0
num_Cl=0
#
# =====> Calcul
#
num_Na=(((concentration/1000.0)*num_wat)/55.55555556)
num_Cl=(((concentration/1000.0)*num_wat)/55.55555556)
if glob_charge >= 0:
    num_Na=(num_Na-glob_charge)
if glob_charge <= 0:
    num_Cl=(num_Cl+glob_charge)
num_Na=int(num_Na+0.5)
num_Cl=int(num_Cl+0.5)
#print("You have to add ",num_Na," Na+")
#print("You have to add ",num_Cl," Cl-")
#
# =====> Write results in ionize.results.txt 
#
valeurs=[str(num_Na), str(num_Cl)]
with open("ionize.results.txt", "w") as filout:
    for val in valeurs:
      filout.write(f"{val}\n")
#




    
   
          
