import random
import math
print ("Enter the number of players in your raid")
raiders = float (input())
if raiders > 30:
    print('Error, Try again.')
else:      
    def fire_standing (a):
        if a == 0:
            return 'Invaild Data, Restart'
                    #debugging
        if a == 1:
          return a * 0.25
        else:
            return a / (0.0125 * math.pow((a-0), 2) + 0 )
            #0.25 is the factor ratio between amount of players taking fire damage and 20 man raid
    
    def Distance_Factor (b):
        if b >= 1:
            return 'Error'
        else:
            return (random.randint(0, 10) + b ) / 10
    
    def Fire_Bomb (c):
        return (c * random.random()) + (c * random.random()) + (c * random.random()) + (c * random.random())
    
    def Immolation (d):
        return d * random.randint (0, 9)
    
    def Pounding (e):
        return e * 91800
    
    def Barrage (f):
        return 190000 * f
    if raiders == 20:    
        y = Distance_Factor (0) + fire_standing (1) + Fire_Bomb (1) + Immolation (1) + Pounding (1) + Barrage (1)
        z = "Is the estimated damage your raid will take"
        print (round(y, 0), z)
    else:
        h = Distance_Factor (0) + fire_standing (raiders) + Fire_Bomb (1) + Immolation (1) + Pounding (1) + Barrage (1)
        i = "Is the estimated damage your raid will take"
        print (round(h, 0), i)
    #don't do this, this is very painful to debug
input('Press ENTER to exit')