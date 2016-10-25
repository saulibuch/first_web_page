# -*- coding: UTF-8 -*-
from sys import argv

script, filename = argv 

# vypíšu jméno souboru uvedeného jako parametr za jménem skriptu
print ("New I'm going to erase %r." % filename  )
print ("If you don't want to do that, hit CTRL-C (^C).")
print ("If you want to do that, hit RETURN.")

# vyžádám si reakci uživatele. Dám mu možnost skript pøerušit
input("?")

# otevøu soubor pro zápis
print ("Opening the file...") 
target = open(filename, 'w')

# oøežu soubor, bez parametru je to na velikost 0
print ("Truncating the file. Goodbye!")
target.truncate()

# vyžádám vstup od uživatele - 3 øádky
print ("Now I'm going to ask you for three lines.") 

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print ("I'm going to write these to the file.")

# uložím 3 øádky do souboaru; pozor, øádky nemají konce
target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print ("And finally, we close it.")
target.close()

