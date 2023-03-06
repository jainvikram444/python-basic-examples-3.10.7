import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

#average value of array values
mean_speed = numpy.mean(speed)
print("Mean value of ", speed, " is " , mean_speed)

#middle value of sorting array values
median_speed = numpy.median(speed)
# sorting the array: 77, 78, 85, 86, 86, 86, 87, 87, 88, 94, 99, 103, 111
print("Median value of ", speed, " is " , median_speed)

#If there are two numbers in the middle, divide the sum of those numbers by two.
speed1 = [77, 78, 85, 86, 86, 86, 87, 87, 94, 98, 99, 103]
#(86 + 87) / 2 = 86.5
median_speed1 = numpy.median(speed1)
print("Median value of ", speed1, " is " , median_speed1)






