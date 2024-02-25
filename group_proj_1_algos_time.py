from random import randint
from timeit import repeat

def insertion_sort(arr, key=lambda x: x):
    for i in range(1, len(arr)):
        key_value = arr[i]
        j = i - 1
        while j >= 0 and key(arr[j]) > key_value:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_value

def merge_sort(arr, key=lambda x: x):
    if len(arr) > 1:
        mid = len(arr) // 2
        L, R = arr[:mid], arr[mid:]
        merge_sort(L, key)
        merge_sort(R, key)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if key(L[i]) < key(R[j]):
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def quick_sort(arr, key=lambda x: x):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if key(x) <= key(pivot)]
        greater = [x for x in arr[1:] if key(x) > key(pivot)]
        return quick_sort(less, key) + [pivot] + quick_sort(greater, key)

def run_sorting_algorithm(algorithm, array):
    setup_code = f"from __main__ import {algorithm}"
    stmt = f"{algorithm}({array})"
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)} seconds")


def main():
    array_size = int(input("Enter the size of the array: "))
    array_list = [randint(0, 1000) for _ in range(array_size)]

    sorting_algorithms = {
        '1': insertion_sort,
        '2': merge_sort,
        '3': quick_sort,
    }

    print("\nChoose the algorithm\n1. Insertion\n2. Merge\n3. Quick\n")
    choice = input("Enter the choice: ")

    sorting_algorithm = sorting_algorithms.get(choice)
    if sorting_algorithm:
        run_sorting_algorithm(sorting_algorithm.__name__, array_list)
    else:
        print("Invalid choice. Please choose a valid sorting algorithm.")

if __name__ == "__main__":
    main()
