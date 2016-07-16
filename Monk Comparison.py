spell = input("Please Enter your Spell Power rating: ")
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
		
	

	
		
def Comparison (c):
	if c == 0:
		return 'Fail'
	else:
		return (Essence (c) - Vivify (c))

		
		
		
		
input('Press ENTER to exit')