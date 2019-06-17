adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]

option='''1) print only those numbers greater than 5 
	  2) also print those numbers those are less than or equals to 2 ( <= 2 ) 
	  3) store these answers in in two different list also'''

print(option)
x=int(input("Enter choice:"))

def switch(argument):
	switcher={
		1: for i in adhoc:
				if i>5:
					print(i),
		2: for i in adhoc:
				if i<=2:
					print(i),
		3:
			for i in adhoc:                                                                                                                      				if i>5:                                                                                                                                                   print(i)
					y=[]
					y.append(i)   
 			for i in adhoc:                                                                                                                      
                        	if i<=2:                                                                                                                      
                                	print(i)  
					z=[]
                                	z.append(i)
			print(y,z)
	print(switcher.get(1,"invalid choice"))

switch(x)
