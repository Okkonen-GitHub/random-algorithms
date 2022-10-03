import random

# listan pituus ja listan alkioden arvot ovat satunnaislukuja väliltä [-N, N]
N = 12


def bubble_sort(array: list) -> list: 
        
    arrlen = len(array)
    for _ in range(arrlen):
        for j in range(arrlen-1):
            if array[j] > array[j+1]:
                tmp = array[j]
                array[j] = array[j+1]
                array[j+1] = tmp
        
    return array


unsorted_list = [random.randint(-N, N) for _ in range(N)]
correct_solution = unsorted_list.copy()
correct_solution.sort() # lajitellaan luvut sisäänrakennetulla sort() komennolla, jota voidaan verrata itse lajiteltuun listaan
print("Generated list", unsorted_list)

sorted = bubble_sort(unsorted_list)

print("Sorted list", sorted)

print("correct:", correct_solution == sorted)
