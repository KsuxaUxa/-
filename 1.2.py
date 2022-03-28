cubes = [x· *3 для x в диапазоне (100), если  x%2 != 0 ]
print('Cоздан список кубов нечётных чисел {}'.format(cubes))
my_numbers_sum = 0
my_numbers_sum_list=[]

# итерация по списку
для i в диапазоне(len(cubes)):
    # print ('- - - print cubes [i]', cubes [i])
    my_str = str(cubes[i])
    my_list = список(my_str)
    # print ('print my_list', my_list)
    для i в диапазоне(len(my_list)):
        my_list[i] = int(my_list[i])
    # Вычислить сумму чисел (вар.1)
    '''
 my_numbers_sum = сумма(my_list)
 print (my_numbers_sum)
    '''
    # Вычислить сумму чисел (вар.2)
    для i в диапазоне(len(my_list)):
        my_numbers_sum = my_numbers_sum + my_list[i]

    #Условие,сумма чисел делится нацело на 7
    если my_numbers_sum % 7 == 0:
        print('Cумму чисел, делящихся на 7 : ',my_numbers_sum)
        my_numbers_sum_list.append(my_numbers_sum)

print('Список чисел, делящихся на 7 (задание 1) : ',my_numbers_sum_list)