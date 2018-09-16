## Rough attempt to estimate how much time all the water dumped by Hurricane Florence (or a regular storm, for comparison) would take to be pumped somewhere else
import numpy as np
import matplotlib.pyplot as plt

# Inputs
aqueductCapacity = 370 	#[m^3/s] capacity of CA aqueduct per Wikipedia
florenceRainfall = 18e12/7 #[gallons] average volume of water dumped by Florence in one day (18 trillion over 7 days): https://mobile.twitter.com/RyanMaue/status/1040467582120337408
regularRainfall = 3.473712e9 #[gallons] volume of water dumped by a regular storm (2" over 10x10mile area) https://water.usgs.gov/edu/activity-howmuchrain.php
lakeMeadVolume = 32.22 #[km^3] cubic kilometers of water that can be stored in Lake Mead

# Conversions
gallonsToSI= 264.17 	#[gallons/m^3]
florenceRainfall = florenceRainfall/gallonsToSI
regularRainfall=regularRainfall/gallonsToSI
lakeMeadVolume=lakeMeadVolume*1000**3 #[m^3]

# Amount of time to pump different volumes in hours or days
timeToPump = florenceRainfall/aqueductCapacity #[s] time to pump all that rainwater in seconds
timeToPump = timeToPump/3600 #[hours] time to pump all that rainwater in hours
print(str(np.round(timeToPump,2))+' hours (Florence)')
timeToPump = timeToPump/24 #[days]
print(str(np.round(timeToPump,2))+' days (Florence)')

timeToPumpRegular = regularRainfall/aqueductCapacity
timeToPumpRegular = timeToPumpRegular/3600 #[hours] time to pump all that rainwater in hours
print(str(np.round(timeToPumpRegular,2))+' hours (regular storm)')
timeToPumpRegular = timeToPumpRegular/24 #[days]
print(str(np.round(timeToPumpRegular,2))+' days (regular storm)')

# Number of California aqueducts to pump in reasonable amount of time
# Move all that water in N days
numberOfDaysToMoveWater = 2
numberAqueducts = timeToPump/numberOfDaysToMoveWater
print(str(np.round(numberAqueducts,2))+ ' CA aqueducts to move water in '+str(np.round(numberOfDaysToMoveWater,2))+' day(s)')

# How many days of Florence fit into Lake Mead?
numberFlorencesStored = florenceRainfall/lakeMeadVolume
print(str(np.round(numberFlorencesStored,2))+' days of Florence stored in Lake Mead')
