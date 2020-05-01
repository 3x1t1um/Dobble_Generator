import platform
import os
from datetime import datetime

def launch():
	banner = """	██████╗  ██████╗ ██████╗ ██████╗ ██╗     ███████╗
	██╔══██╗██╔═══██╗██╔══██╗██╔══██╗██║     ██╔════╝
	██║  ██║██║   ██║██████╔╝██████╔╝██║     █████╗
	██║  ██║██║   ██║██╔══██╗██╔══██╗██║     ██╔══╝
	██████╔╝╚██████╔╝██████╔╝██████╔╝███████╗███████╗
	╚═════╝  ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚══════╝

                   \033[31m{ By AskaD }\033[00m
              [=] \033[34mAuthor\033[00m  : AskaD    [=]
                 { \033[34mGithub\033[00m : 3x1t1um }"""

	if 'Windows' in platform.platform():
		os.system('cls')
	else:
		os.system('clear')

	print(banner)

	return datetime.now().strftime("%H:%M:%S")
