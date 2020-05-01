from src.generate_number import *
from src.launcher import *
from src.placing_image import *
import sys

if __name__ == '__main__':
	input_time = launch()

	print()
	print('\033[31m[ * ]\033[00m \033[38;5;82mPlease enter a number according to the instructions\033[00m')
	print()

	try:
		nb = int(input('[\033[34m'+input_time+'\033[00m] \033[31m~#\033[00m '))

	except KeyboardInterrupt:
		print('\033[31m[ ! ]\033[00m \033[38;5;82mCanceled by user\033[00m')
		sys.exit(1)

	except:
		print('\033[31m[ ! ]\033[00m \033[38;5;82mMust be a number\033[00m')
		sys.exit(1)

	data = main(nb)
	generate_image_from_list(data)
