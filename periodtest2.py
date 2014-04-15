def max_period_list(T, t0, timestamps, t_max):
    period_list = []
    T = T*1.0
    for a in range(np.ceil(t_max/T).astype(int)): #t_max is range because that is the maximum value in the system
    	period_list += [t0 + a*T] #adds the value to the list of potential periods
    return period_list

def min_period_list(timestamps, period_list, t_min):
    length = len(period_list)
    for a in range(length -1):
        if period_list[a] < t_min: #tests if any value is smaller than smallest data point
            period_list.pop(a) #deletes that data point
            end_add = "yes"
        else:
            end_add = "no"
        if end_add == "yes": #prevents t_min from being added multiple times
            period_list.insert(0, t_min)
    print(period_list)
    return period_list

def order_timestamps(timestamps): #orders timestamps into sublist pairs
    new_timestamps = [timestamps[i:i+2] for i in range(0, len(timestamps)-1, 2)]
    return new_timestamps

def period_test(T, t0, timestamps, period_list): #tests if a potential value appears in a segment where it cannot
    Indicator = 0 #binary switch that determins if a potential period is viable
    for q in period_list:
        for a in range(len(timestamps)): #runs through each pair of times representing one segment
            t1 = timestamps[a][0]
            t2 = timestamps[a][1]
            if t1 <= q <= t2: #tests if a period list value lies in a segment
                Indicator = 1 
    return Indicator
        
def period(T, t0, timestamps): #runs all of the functions for one specific T and t0 value
    t_max = timestamps[-1]
    t_min = timestamps[0]
    plist1 = max_period_list(T, t0, timestamps, t_max)
    plist2 = min_period_list(timestamps, plist1, t_min)
    timestamps = order_timestamps(timestamps)
    Indicator = period_test(T, t0, timestamps, plist2)
    return Indicator
    
def overall_period(timestamps): #runs the program over all the default parameters
   fractions = []

   for T in range(1,201): #default 8 years for a period
        t0_values = []
        for t0 in range(T):
             Indicator = period(T, t0, timestamps)
             if Indicator == 0:
                 t0_values += [t0]
        #f.write(repr(T) + repr(t0_values) + '\n')
        print(T)#prints all the t0 values that work with that specific T
        for q in t0_values:        	
            ax0.plot(T, q, 'k.') #graphs each looped point
        fraction = 1-(len(t0_values)/float(T))
        fractions += [fraction]
        ax1.semilogy(T, fraction, 'k.') #graphs the fraction of t0 that work
        #ax2.plot(T, fraction, 'k.') #graphs the ln fraction of t0 that work
   return fractions #returns to be multiplied with geometric_probability and graphed
        

def geometric_probability(transit_fractions, StarMass, StarRadius): 
#calculates chance of planet appearing to Kepler
	for T in range(1,201):
		T_years = T/365. #converts period to years
		print(T)
		print(T_years)
		a = ((T_years**2.)*StarMass)**(1./3)
		Prob_Percent = (StarRadius/a) #radius must be in AU
		print(a)
		print(Prob_Percent)
		ax1.semilogy(T, Prob_Percent, 'b.',)
		total_fraction = Prob_Percent*transit_fractions[T-1]
		print(total_fraction)
		ax1.semilogy(T, total_fraction, 'r.',)
		

        

#The program with a set value of timestamps   
import numpy as np
import matplotlib.pyplot as plt
import cProfile, pstats, StringIO
pr = cProfile.Profile()
pr.enable()
# ... do something ...

     
timestamps = [5, 90, 93, 183, 186, 276, 279, 369]


fig1 = plt.figure(1, figsize = (10,10))
ax1 = fig1.add_subplot(2,1,2) #graph for fraction of t0 values
ax0 = fig1.add_subplot(211, sharex = ax1)#graph for accepted t0 values



StarMass = 1 #Scaled to Sun, temporarily using mass of sun
StarRadius = 0.00929826069 #in AU, temporarily using radius of sun
#f = open('testfile.txt','w')
transit_fractions = overall_period(timestamps)
geometric_probability(transit_fractions, StarMass, StarRadius)
#f.close()


#Plotting description for the accepted t0 values
ax0.set_ylabel('Period Displacements (t0)')
ax0.set_title('Testing Viable Periods Over Transit Data\nTimestamps: {0:s}'.format(timestamps))
#Plotting description for the fraction of viable t0 values
ax1.set_xlabel('Period Lengths (T)')
ax1.set_ylabel('Fraction')
ax1.set_ylim(ymax=1.1, ymin = -1.1)

ax1.set_title('Fraction of Planetary Transits Detected')
ax1.text(1,0.5,'Black = Transit Prob \n Blue = Geometric Prob \n Red = Total Prob', horizontalalignment='right', verticalalignment='center', transform=ax1.transAxes)
plt.show()



pr.disable()
s = StringIO.StringIO()
sortby = 'cumulative'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print s.getvalue()


            


            
    
    
