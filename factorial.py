def factorial(n):
	fact = 1
	for i in range(1,n+1): 
		fact = fact * i 
	print (f'The factorial of {str(n)} is {str(fact)}')

factorial(6)
