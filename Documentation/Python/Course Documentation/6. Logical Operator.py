# Sixth Real Python Project

'''
# Tutorial 1
temp = 20
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")
'''

# Tutorial 2
temp = 20
is_sunny = False

# Is Sunny
if temp >= 28 and is_sunny:
    print("It's HOT outside"
          "\nIt's SUNNY")
elif temp <= 0 and is_sunny:
    print("It's COLD outside"
          "\nIt's SUNNY")
elif 28 > temp > 0 and is_sunny:
    print("It's WARM outside"
          "\nIt's SUNNY")

# Is Cloudy
if temp >= 28 and not is_sunny:
    print("It's HOT outside"
          "\nIt's CLOUDY")
elif temp <= 0 and not is_sunny:
    print("It's COLD outside"
          "\nIt's CLOUDY")
elif 28 > temp > 0 and not is_sunny:
    print("It's WARM outside"
          "\nIt's CLOUDY")