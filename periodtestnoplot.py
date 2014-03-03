def max_period_list(T, t0, t_max):
    period_list = []
    for a in range(np.ceil(t_max/T).astype(int)): #t_max is range because that is the maximum value in the system
        if (t0 + a*T) <= t_max: #tests if period value surpasses maximum data point
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
    plist1 = max_period_list(T, t0, t_max)
    plist2 = min_period_list(timestamps, plist1, t_min)
    timestamps = order_timestamps(timestamps)
    Indicator = period_test(T, t0, timestamps, plist2)
    return Indicator
    
def overall_period(timestamps): #runs the program over all the default parameters
   for T in range(1,4001): #default 8 years for a period
        t0_values = []
        for t0 in range(T):
             Indicator = period(T, t0, timestamps)
             if Indicator == 0:
                 t0_values += [t0]
        print(T)
        fraction = len(t0_values)/float(T)

def geometric_probability(StarMass, StarRadius): 
#calculates chance of planet appearing to Kepler
	for T in range(1,1):
		T_years = T/365. #converts period to years
		print(T)
		print(T_years)
		a = ((T_years**2.)*StarMass)**(1./3)
		Prob_Percent = (StarRadius/a)*100 #radius must be in AU
		print(a)
		print(Prob_Percent)

        

#The program with a set value of timestamps   
import numpy as np
import matplotlib.pyplot as plt
import cProfile, pstats, StringIO
pr = cProfile.Profile()
pr.enable()
# ... do something ...

     
timestamps = [5, 90, 93, 183, 186, 276, 279, 369]


StarMass = 1 #Scaled to Sun, temporarily using mass of sun
StarRadius = 0.00929826069 #in AU, temporarily using radius of sun

overall_period(timestamps)




pr.disable()
s = StringIO.StringIO()
sortby = 'cumulative'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print s.getvalue()


            


            
    
    
