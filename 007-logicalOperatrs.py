# 'or' Operator
temp = 25
is_raining = True

if is_raining or temp > 35 or temp < 0 :
    print("Outdoor event is cancelled")
else :
    print("the outdoor event occur as per the schedule ")

# 'and' Operator
temp = 35
is_sunny = True
if temp > 28 and is_sunny :
    print("its too hot out side ") 
elif temp <= 0 and is_sunny :
    print("Its cold outside  ")

# 'not'
print(bool(not(24)))
