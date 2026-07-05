x = int(input("Enter your number: "))
if x<0:
	x= x*-1
	print("\nNumber changed to positive")
elif x==0:
	print("Null value")
elif x==42:
	x = x**2
	print("\tYou hit a bumper.\nyou got it!")
else: print("try again")
