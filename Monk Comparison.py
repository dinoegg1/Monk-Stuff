print ("Please Enter your Spell Power rating")
spell = float (input())
def Essence(a):
	if a == 0:
		return 'Fail'
	else:
		return ((1.10 * a) + (0.36 * a)) * 6	
		
def Vivify (b):
	if b == 0:
		return 'Fail'
	else:
		return ((b * 2.75) * 3)
				
y = Essence(spell) - Vivify(spell)
print(y)

	
input('Press ENTER to exit')