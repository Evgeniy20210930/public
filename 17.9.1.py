import sys
elements = input('Введите числа через пробел:').split()
elem = int(input('Введите число:'))

def sort(elements):
   int_list = [int(i) for i in elements]
   for i in range(len(int_list)):
      for j in range(len(int_list)-i-1):
        if int_list[j] > int_list[j+1]:
            int_list[j], int_list[j+1] = int_list[j+1], int_list[j]
   return (int_list)

def binary_search(array, elem, left, right):
    if left > right:  # если левая граница превысила правую,
        print ('Введенное число отсутствует в списке')#False  # значит элемент отсутствует
        sys.exit()
    middle = (right + left) // 2  # находимо середину
    if array[middle] == elem:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif elem < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, elem, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, elem, middle + 1, right)

bs = binary_search(sort(elements), elem, 0, len(sort(elements))-1)
before_elem = 'Номер позиции элемента ' + str(sort(elements)[bs-1])+', который меньше введенного пользователем числа:' + str(bs-1)
after_elem = 'Номер позиции элемента ' + str(sort(elements)[bs+1])+', который больше или равен введенному пользователем числа:' + str(bs+1)
print('Отсортированный список: ' + str(sort(elements)))
print('Номер позиции элемента, введенного пользователем: ' + str(bs))
if bs-1 < 0:
   print ('Нет числа меньшего, введенного пользователем')
else:
    print(before_elem)

if len(sort(elements)) <= bs:
    print('Нет числа большего, введенного пользователем')
else:
    print(after_elem)


