#datetime classes in Python are categorized into 5 main classes.
#date - Manipulate just date(Month, day, Year)
#time - Time Time independent of the day(Hour, minute, second, microsecond)
#datetime - Combination of time and date(Month, day, year hour, minute, second, microsecond)
#timedelta - A duration of time  used for manipulating dates
#tzinfo - An abstract class for dealing with time zones.


#TICK
#Floating-point numbers in units of seconds for time interval are indicated by Tick in python. They are expressed in seconds since 12.00am, #Jan 1, 1970(epcoh).
#The function time.time() returns the current system time in ticks since 12:00am, Jan 1, 1970(Epoch).
import time
ticks=time.time()
print("Number of ticks since 12:00am, Jan 1,1970",ticks)

#TIME TUPLE
#Python's time functions handle time as a tuple of 9 numbers:
#Index 0 to 9

