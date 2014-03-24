import pyfits
import kplr
import matplotlib.pyplot as plt
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

for y in range(len(flux)):
	plt.plot(time[y],flux[y],'r.')
plt.axhline(y=0,xmin=0,xmax=1)
plt.title('Lightcurves for KOI 3335426')
plt.xlabel('Time (Days)')
plt.ylabel('Flux')
plt.show()