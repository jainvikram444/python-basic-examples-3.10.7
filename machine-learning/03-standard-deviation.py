import numpy

speeds1 = [32,111,138,28,59,77,97]
speeds2 = [86,87,88,86,87,85,86]

#Standard deviation is a number that describes how spread out the values are.
#A low standard deviation means that most of the numbers are close to the mean (average) value.
#A high standard deviation means that the values are spread out over a wider range.

var_speed1 = round(numpy.std(speeds1),1)
print("Variance value of ", speeds1, " is " , var_speed1)

std_speed1 = round(numpy.var(speeds1),1)
print("Standard Deviation value of ", speeds1, " is " , std_speed1)

#now can we breackdown the process for speeds1
print("=======================now can we breackdown the process for speeds1================================")
mean_speed1 = 0.0
for speed in speeds1:
    mean_speed1 += speed
mean_speed1 = round(mean_speed1/len(speeds1), 1)
print("Mean value of ", speeds1, " is " , mean_speed1)

dist_speed1 = []
for speed in speeds1:
    dist_speed1.append(round(speed - mean_speed1,1))
print("Diff from the mean value of ", mean_speed1, " is " , dist_speed1)

for indx1, speed in enumerate(dist_speed1):
    dist_speed1[indx1] = round(speed*speed,1)
print("Square value (distance array) of ", speeds1, " is " , dist_speed1)

mean_dist_speed1 = 0.0
for speed in dist_speed1:
    mean_dist_speed1 += speed
mean_dist_speed1 = round(mean_dist_speed1/len(dist_speed1), 1)
print("Mean distance value of ", dist_speed1, " is " , mean_dist_speed1)

square_root_dist_speed1 = round(numpy.sqrt(mean_dist_speed1),1)
print("Square root(distance) value of ", dist_speed1, " is " , square_root_dist_speed1)


print("=======================================================")
#==================================================================
var_speed2 = round(numpy.std(speeds2),2)
print("Variance value of ", speeds2, " is " , var_speed2)

std_speed2 = round(numpy.var(speeds2),2)
print("Standard Deviation value of ", speeds2, " is " , std_speed2)

#now can we breackdown the process for speeds2
print("=======================now can we breackdown the process for speeds2================================")
mean_speed2 = 0.0
for speed in speeds2:
    mean_speed2 += speed
mean_speed2 = round(mean_speed2/len(speeds2), 2)
print("Mean value of ", speeds2, " is " , mean_speed2)

dist_speed2 = []
for speed in speeds2:
    dist_speed2.append(round(speed - mean_speed2, 2))
print("Diff from the mean value of ", mean_speed2, " is " , dist_speed2)

for indx2, speed in enumerate(dist_speed2):
    dist_speed2[indx2] = round(speed*speed,2)
print("Square value (distance array) of ", speeds2, " is " , dist_speed2)

mean_dist_speed2 = 0.0
for speed in dist_speed2:
    mean_dist_speed2 += speed
mean_dist_speed2 = round(mean_dist_speed2/len(dist_speed2), 2)
print("Mean distance value of ", dist_speed2, " is " , mean_dist_speed2)

square_root_dist_speed2 = round(numpy.sqrt(mean_dist_speed2),2)
print("Square root(distance) value of ", dist_speed2, " is " , square_root_dist_speed2)
