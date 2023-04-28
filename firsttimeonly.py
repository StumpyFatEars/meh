import time
import os
import time

firsttime = " "

f = open("__.txt", "a+")
f.close()

time.sleep(2)



f = open("__.txt", "r")
if (f.read(5)) == "x8Tk0":
	print("Welcome!")
	firsttime = False

elif (f.read(5)) == "":
	print("That Was Your First Time!")
	firsttime = True

else:
	print("Error")
	f.close()
	__END__
	
	
	
	
time.sleep(2)

if firsttime == True:
	f = open("__.txt", "w")
	f.write("x8Tk0")
	f.close()
	os.system("register.py")
	
elif firsttime == False:
	f.close()
	os.system("login.py")