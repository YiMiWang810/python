s = 100;
h = s/2;
for n in range(2,11):
	s = s+2*h;
	h = h/2;
print("total of road is %f"%s)
print("The tenth is %f"%h)