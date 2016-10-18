# -*- coding: utf-8 -*-
name = 'Zed A. Shaw'
age = 35 #Not a lie
height = 74 #inches
height_in_cm = height * 2.54
weight = 180 #lbs
weight_in_kg = weight * 0.45359237
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print ("Let's talk about %s." % name )
print ("He's %f centimeters tall." % height_in_cm )
print ("He's %f kilograms heavy." % weight_in_kg )
print ("Actually that's not too heavy.")
print ("He's got %s eyes and %s hair." % (eyes, hair) )
print ("His teeth are usually %s depending on the coffee." % teeth )

print ("If I add %d, %f and %f I get %r." % (age, height_in_cm, weight_in_kg, age + height_in_cm + weight_in_kg) ) 
