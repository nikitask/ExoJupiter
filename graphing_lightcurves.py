import pyfits
import kplr
import matplotlib.pyplot as plt
import numpy as np
import os.path
os.path.exists("lightcurve_data.txt")
if os.path.exists("lightcurve_data.txt"):
	file = open("lightcurve_data.txt", 'r')
	t = file.readline()
	t = t.split(',')
	t_freq = file.readline()
	t_freq = t_freq.split(',')
	a = []
	b = []
	for w in t:
		w.rstrip('\n')
		w = float(w)
		a += [w]
	for w in t_freq:
		w.rstrip('\n')
		print(w)
		w = float(w)
		b += [w]
	plt.plot(a, b, 'r.')
	
	plt.title("Testing 30 Hour Transits")
	plt.xlabel("t1 (Hours)")
	plt.ylabel("Number of Time points within Range")
	plt.ylim(-20,np.max(b)+10)
	plt.show()
		
else: 
	file = open("lightcurve_data.txt", 'w')
	client = kplr.API()
	name = 3335426
	stars = client.star(name)
	lcs=stars.get_light_curves(True)

	time,flux,ferr,quality = [],[],[],[]
	for lc in lcs:
		with lc.open() as f:
			hdu_data=f[1].data
			time.append(hdu_data["time"])
			flux.append(hdu_data["sap_flux"])
			ferr.append(hdu_data["sap_flux_err"])
			quality.append(hdu_data["sap_quality"])

#for y in range(len(flux)):
	#plt.plot(time[y],flux[y],'r.')
#plt.axhline(y=0,xmin=0,xmax=1)
#plt.title('Lightcurves for KOI 3335426')
#plt.xlabel('Time (Days)')
#plt.ylabel('Flux')
#plt.show()

	w = []
	for a in time:
		w = np.concatenate([w,a])
	w = w*24
	print(w)

	t1 = -0.25*24
	t2 = 1*24 #steps third the size, would these transits be in the dat, are the transits in the data
	t = []
	t_freq = []
	while t1 <= 1600*24:
		freq = 0
		for a in w:
			if a >= t1:
				if a <= t2:
					freq += 1
		t += [t1]
		t_freq += [freq]
		print(t1)
		t1 += 1.25*24
		t2 += 1.25*24
	t = str(t).strip('[]')
	t_freq = str(t_freq).strip('[]')
	file.write(t+ '\n' + t_freq)
	file.close()
