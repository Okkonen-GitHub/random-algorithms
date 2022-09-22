import random, math

N = 12


def sel_sort(array: list) -> list: 
        

    arrlen = len(array)
    for i in range(arrlen):
        for j in range(i, arrlen):
            if array[j] < array[i]:
                tmp = array[i]
                array[i] = array[j]
                array[j]=tmp

    
    return array
        


unsorted_list = [random.randint(-N, N) for i in range(N)]
correct_solution = unsorted_list.copy()
correct_solution.sort()
print("Generated list", unsorted_list)

sorted = sel_sort(unsorted_list)

print("Sorted list", sorted)

print("correct? ", correct_solution == sorted)