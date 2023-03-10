sequence = input('Введите последовательность чисел через пробел ')
def is_int(str):
    str = str.replace(' ', '')
    try:
        int(str)
        return True
    except ValueError:
        return False
if " " not in sequence:
    print('ОТСУТСТВУЮТ ПРОБЕЛЫ')
    sequence = input('Введите целые числа через пробел: ')
if not is_int(sequence):
    print('Введенные символы не соответствуют условию ввода')
else:
    # sequence_numbers = sequence_numbers.split()
    list = [int(item) for item in sequence.split()]
    sequence_list = []
    for item in list:
        if item not in sequence_list:
            sequence_list.append(item)

def sorting_sequence_list():
    for i in range(len(sequence_list)):

        for j in range(len(sequence_list) - i - 1):
            if sequence_list[j] > sequence_list[j + 1]:
                sequence_list[j], sequence_list[j + 1] = sequence_list[j + 1], sequence_list[j]

    print(sequence_list)

sorting_sequence_list()

left = 0
right = len(sequence_list)
number = int(input('Введите произвольное чило '))

def binary_search(sequence_list, number, left, right):
    if left > right:
        return False
    while left < right - 1:
        middle = (right + left) // 2
        if number < sequence_list[middle]:
            right = middle
        else:
            left = middle
    return left
i = binary_search(sequence_list, number, left, right)
print(i)

if number < min(sequence_list):
    print(f'Число {number} минимального в последовательности')
if number > max(sequence_list):
    print(f'Число {number} максимального в последовательности')
