#saving for imports
import random
print ("Enter the amount of players in your raid")
raiders = float ( input ()) 
#this is the idiot factor
def fire_standing (a):
	if a == 0:
		return 'Invaild Data, Restart'
				#debugging
	else:
		return a * 0.25
		#0.25 is the factor ratio between amount of players taking fire damage and 20 man raid
z = fire_standing (raiders)
print (z)
print ("This is the average amount of players that will stand in fire")
def Distance_Factor (b):
	return ( random.randint(0, 10) + b ) / 10
#Artillery
y = Distance_Factor (0) * z * 210000
#Blitz & Dot
x = (z * 70000) + (160500 * z)
#Falling Slam
w = 45000
#Extra Falling Slam
v = 300000 * z
def Fire_Bomb (b):
	return b * random.randint (0, 4)
	#Add independent rolls for each bomb max 4
FireBomb = Fire_Bomb (142857)
def Immolation (a):
	return a * random.randint (0, 9)
	#Add independent rolls for each Fire max 9
i = Immolation (raiders)
def Pounding (a):
	return a * 91800
	
Pound = Pounding (raiders)
def Unstable_Orb (a):
	return a * random.randint(0, 9)
	#Add independent rolls max 9
Orb = Unstable_Orb (raiders)
Barrage (a):
	return 190000 * a
	
u = Barrage (raiders)
#Air Phase: y, w, v, FireBomb, i
#Ground Phase: x, u, Orb, i, Pound
#1 cycle = 200 seconds
