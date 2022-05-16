numbers = list(map(int, input("Введите последовательность чисел через пробел: ").split()))

for i in range(1, len(numbers)):
    x = numbers[i]
    idx = i
    while idx > 0 and numbers[idx-1] > x:
        numbers[idx] = numbers[idx-1]
        idx -= 1
    numbers[idx] = x

print('Сортировка списка', numbers)

left = 1
right = len(numbers)


def binary_search(numbers, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if numbers[middle] == element:
        return middle
    elif element < numbers[middle]:
        return binary_search(numbers, element, left, middle - 1)
    else:
        return binary_search(numbers, element, middle + 1, right)


element = int(input("Введите число в диапазоне последовательности: "))
print("Индекс элемента:", binary_search(numbers, element, 0, len(numbers)))

