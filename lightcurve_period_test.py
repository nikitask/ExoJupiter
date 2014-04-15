import pyfits
import kplr
import matplotlib.pyplot as plt
import numpy as np
import os.path

file = open("Lightcurve_Data.txt", 'r') #reads in data from graphing_lightcurves.py
t = file.readline()
t = t.split(',')
t_freq = file.readline()
t_freq = t_freq.split(',')
t_list = []
f_list = []
for w in t:
	w.rstrip('\n')
	w = float(w)
	t_list += [w]
for w in t_freq:
	w.rstrip('\n')
	w = float(w)
	f_list += [w]

lim = 55 #Threshold of frequency
for a in f_list:
	if a < lim: #tests if there is a potential transit
		num = f_list.index(a)
		t1 = t_list[num] #finds the time it occured
		for t in range(1,10000): #period lengths
			mult = 1
			while t1+mult*t <= t_list[-1]: #prevents testing past the max time Kepler measured
				c = t1 + mult*t
				c = int(c) #converts to integer
				try: #if the new specific time was not measured by Kepler, it is skipped
					d = t_list.index(c)
					if f_list[d] == a: #tests if the recurring value matches up with previous 
						test = "yes"
						mult += 1
					else:
						test = "no"
						mult = 10000000000000000 #stops the while loop
				except:
					mult += 1
					test = "yes" #if all other transits were not detected, then it is still possible for a planet to have that period
			if test == "yes":
				plt.plot(a, t, 'b.')
plt.show()
				
				