from src.make_list_dobble import *

def main(number):
	global first, seconde, var

	first = 0
	seconde = first + 1
	var = 0

	while var < number:
		if int((first * seconde) / 2) > number:
			break

		var = int((first * seconde) / 2)
		first = first + 1
		seconde = seconde + 1

	if int(var) is not number:
		print(f'\n\033[31m[ + ] Number not in the list\n\n\033[00m\033[34mNew number :\033[00m {var}\n')
	else:
		print('\n\033[31m[ + ] Number in the list\033[00m')

	return generatedooble(var, first, seconde)
