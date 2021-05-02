def getVolume(x,y,z):
	floatNum = 0.0
	intNum = 0
	if((type(x) is type(floatNum)) or (type(x) is type(intNum))):
		return x*y*z
	if (x==0 ) or (y==0 ) or (z==0):
		return None
	if (x==0.0 ) or (y==0.0 ) or (z==0.0):
		return None
	elif x < 0:
		x= -1*x
	elif y < 0:
		y =-1*y
	elif z < 0:
		z =-1*z
	elif x < 0.0:
		x = -1.0*x
	elif y < 0.0:
		y = -1.0*y
	elif z < 0.0:
		z =-1.0*z
	return x*y*z
