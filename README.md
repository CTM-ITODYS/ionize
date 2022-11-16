# ionize
Calculation of the required number of ions for a MD

In molecular dynamics simulations, electrostatic are computed with techniques (i.e. PME) which requires the neutrality of the system.

Biomolecules generally bear charges and it is usual to consider the external concentration in order to be as close as possible close to physiological conditions.

To obtain the number of monovalent ions required for a given number of water molecules and a biological system with a defined global charge, we propose this simple script.

This soft is defided into two files:
- ionize.tk.py
- ionize.py

The first program is a graphical user interface that launch the second python script.

To execute:
python ionize.tk.py

Enjoy,
Florent Barbault
