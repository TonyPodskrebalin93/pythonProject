numb = [5, 6, 2, 1, 3, 4]

def bubble_sort(ls): # пузырковая сортировка
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(ls) - 1):
            if ls[i] > ls[i +1]:
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
                swapped = True
    return ls

bubble_sort(numb)
print(numb)


def selection_sort(ls): # сортировка выборкой
    for i in range(len(ls)):
        lowest = i
        for j in range(i +1, len(ls)):
            if ls[j] < ls[lowest]:
                lowest = j
                ls[i], ls[lowest] = ls[lowest], ls[i]
    return ls

selection_sort(numb)
print(numb)

def insertion_sort(ls):# cjhnbhjdrf 
    for i in range(1, len(ls)):
        key = ls[i]
        j = i - 1
        while ls[j] > key and j >= 0:
            ls[j + 1] = ls[j]
            j -= 1
            ls[j + 1] =key
    return ls


insertion_sort(numb)
print(numb)


