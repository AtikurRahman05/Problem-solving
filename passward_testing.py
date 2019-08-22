# Python-Problem-solving
psswr = input("please input your password: ")
l = len(psswr)
if l>=6 and  '! ' in psswr or '@' in psswr or '#' in psswr  or '$'  in psswr or '%' in psswr or '^' in psswr or ' &' in psswr  or '*' in psswr  or  '_'  in psswr  or  '-'  in psswr  or  '+' in psswr or '='in psswr:
	print('strong pass')

else :
	print('Your password is too weak.\nPassword should have 6 characters or more.\nPassword must contain 1 special character and 1 number.')


