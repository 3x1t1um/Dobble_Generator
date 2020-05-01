def generatedooble(nombre, fs, sc):
        to_do_list = 1
        dooble_nb = []
        fstotal = [i+1 for i in range(fs-1)]
        dooble_nb.append(fstotal)

        for i in fstotal:
            intermediate = []
            intermediate.append(int(i))
            dooble_nb.append(intermediate)

        number_already_use = dooble_nb[0][len(dooble_nb[0])-1]

        while True:
        	if to_do_list == len(dooble_nb)-1:
        		break

        	else:
        		number_list_to_modify = to_do_list + 1
        		number_to_put = (fs - 1) - len(dooble_nb[to_do_list])

        		for i in range(number_to_put):
        			number_already_use = number_already_use + 1
        			dooble_nb[to_do_list].append(int(number_already_use))
        			dooble_nb[number_list_to_modify].append(int(number_already_use))
        			number_list_to_modify = number_list_to_modify + 1

        		to_do_list = to_do_list + 1

        print(f'\033[31m[ + ] List created !\033[00m')
        print(str(dooble_nb)+'\n')
        return dooble_nb
