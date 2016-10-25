# -*- coding: UTF-8 -*-
from sys import argv

script, filename = argv 

# vyp�u jm�no souboru uveden�ho jako parametr za jm�nem skriptu
print ("New I'm going to erase %r." % filename  )
print ("If you don't want to do that, hit CTRL-C (^C).")
print ("If you want to do that, hit RETURN.")

# vy��d�m si reakci u�ivatele. D�m mu mo�nost skript p�eru�it
input("?")

# otev�u soubor pro z�pis
print ("Opening the file...") 
target = open(filename, 'w')

# o�e�u soubor, bez parametru je to na velikost 0
print ("Truncating the file. Goodbye!")
target.truncate()

# vy��d�m vstup od u�ivatele - 3 ��dky
print ("Now I'm going to ask you for three lines.") 

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print ("I'm going to write these to the file.")

# ulo��m 3 ��dky do souboaru; pozor, ��dky nemaj� konce
target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print ("And finally, we close it.")
target.close()

