from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

#The Mode value is the value that appears the most number of times:
mod_speed1 = stats.mode(speed)
print("Median value of ", speed, " is " , mod_speed1)