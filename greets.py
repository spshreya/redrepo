import datetime 
currentDT = datetime.datetime.now() 
print(currentDT)
currentDT.hour

if currentDT.hour<12:
	print('good morning')
elif 12<=currentDT.hour<18:
	print('good afternoon')
elif 18<=currentDT.hour<21:
	print('good evening')
else:
	print('good night')

