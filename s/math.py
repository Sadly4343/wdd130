import math
t = float(input("Input wind speed in Miles/hour: "))
v = float(input("Input air temperture in degrees Celcius: "))

wci = 35.74 + 0.6215*t - 35.75(v, 0.16 )+ 0.3965*t*math.pow(v, 0.16)