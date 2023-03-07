import numpy
import math 

ages1 = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

# Let's say we have an array of the ages of all the people that live in a street.
perc_age1 = numpy.percentile(ages1, 75)
print("Percentile 70% of ages ", ages1, " value is ", perc_age1 )

print("=================Breackdown the process for 70%==========================")
perc1 = (len(ages1) * 70) / 100
print("Percentage 70% of ages ", sorted(ages1), " lenght is ", len(ages1)  , " and  value is ", perc1,  int(math.ceil(perc1)) - 1)

perc_index_age1 = 0.0
if perc1.is_integer():
    perc_index_age1 =  sorted(ages1)[int(perc1)]
else:
    perc_index_age1 =  sorted(ages1)[int(math.ceil(perc1))]

print("Percentile 70% of ages ", sorted(ages1), " and  value is ", perc_index_age1)

print("\n======================================================================================\\n")
  
# Let's say we have an array of the ages of all the people that live in a street.
perc_age2 = numpy.percentile(ages1, 90)
print("Percentile 90% of ages ", ages1, " value is ", perc_age2 )

print("=================Breackdown the process for 90%==========================")

perc2 = (len(ages1) * 90) / 100
print("Percentage 70% of ages ", sorted(ages1), " lenght is ", len(ages1)  , " and  value is ", perc2, int(math.ceil(perc2)) - 1)

perc_index_age2 = 0.0
if perc2.is_integer():
    perc_index_age2 =  sorted(ages1)[int(perc2)]
else:
    perc_index_age2 =  sorted(ages1)[int(math.ceil(perc2)-1)]

print("Percentile 90% of ages ", sorted(ages1), " and  value is ", perc_index_age2)
