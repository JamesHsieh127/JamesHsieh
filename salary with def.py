hour= input("hour:" )
rate= input("rate:" )
try:
	h= float(hour)
	r= float(rate)
except:
	print("Error")
	quit()

def computepay(h,r):
	if (0<h<=40):
        		p= float(h*r)
        		return p
	elif (h>40):
       			pay= (r*1.5*h)-(40*r*0.5)
				return pay
	else:
        return print("Error")

print("Pay",computepay(h,r))
