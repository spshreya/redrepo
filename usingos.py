import os
                                                                                                                                                     
x=raw_input("enter string:")
print(type(x))                                                                                                                                                                                                                                                                                            
if x==str(x):
        os.system("useradd Shreya")
	os.system("passwd Shreya")
else:
        print("you did not enter a string")
