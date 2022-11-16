#  
#    **********
#    * ionize *
#    **********
#
# purpose: provide the number of Na+ and Cl-
# ions to add in order to reach a defined concentration
#
#
#
# =====> Import tkinter and subprocess
#
import os, sys
import tkinter 
from tkinter import ttk

numNa="to be calculated"
numCl="to be calculated"

#
# =====> Function calculate
#
def calculate(*args):
  try:
    w=numwat.get()
    q=globcharge.get()
    c=concentration.get()
    os.system(f"python ionize.py {q} {w} {c}")
    #os.system("more ionize.results.txt")
    with open ("ionize.results.txt", "r") as fi:
        data=fi.readlines()
    numNa.set(str(data[0]))
    numCl.set(str(data[1]))
    print(f"number Na {numNa} et number Cl {numCl}")
    #return numNa, numCl
  except ValueError:
    pass
#
# =====> GUI
#
###### creation of the main window

root = tkinter.Tk()
root.title("Ionize")                                     
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(tkinter.N, tkinter.W, tkinter.E, tkinter.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
#
# =====> Global variable declaration
#
numwat = tkinter.StringVar()
globcharge = tkinter.StringVar()
concentration = tkinter.StringVar()
numNa = tkinter.StringVar()
numCl = tkinter.StringVar()

###### 1st line, write the number of water molecules
ttk.Label(mainframe, text="Number of water molecules").grid(column=1, row=1, sticky=tkinter.W)
numwat_entry = ttk.Entry(mainframe, width=7, textvariable=numwat)
numwat_entry.grid(column=2, row=1, sticky=(tkinter.W, tkinter.E))

###### 2nd line, write the desired concentration in nM
ttk.Label(mainframe, text="System global charge").grid(column=1, row=2, sticky=tkinter.W)
globcharge_entry = ttk.Entry(mainframe, width=7, textvariable=globcharge)
globcharge_entry.grid(column=2, row=2, sticky=(tkinter.W, tkinter.E))

###### 3rd line, write the desired concentration in nM
ttk.Label(mainframe, text="Concentration in nM").grid(column=1, row=3, sticky=tkinter.W)
concentration_entry = ttk.Entry(mainframe, width=7, textvariable=concentration)
concentration_entry.grid(column=2, row=3, sticky=(tkinter.W, tkinter.E))

###### 4th line, buttons calculate
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=1, row=4, sticky=tkinter.W)
ttk.Button(mainframe, text="Quit", command=root.destroy).grid(column=4, row=4, sticky=tkinter.W)

###### 5th line, Results
ttk.Label(mainframe, text="Number of Na+ ").grid(column=1, row=5, sticky=tkinter.W)
ttk.Label(mainframe, textvariable=numNa).grid(column=2, row=5, sticky=tkinter.W)
ttk.Label(mainframe, text="Number of Cl- ").grid(column=3, row=5, sticky=tkinter.W)
ttk.Label(mainframe, textvariable=numCl).grid(column=4, row=5, sticky=tkinter.W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)
    numwat_entry.focus()
    root.bind("<Return>", calculate)

###### Execution
root.mainloop()







    
   
          
