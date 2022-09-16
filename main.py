# Enunciado: Crea una función que ordene y retorne una lista de números.
# - La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro adicional
#   "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor o de mayor a menor.
# - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.

def swap_elements(array, pos1, pos2):
    array[pos1], array[pos2] = array[pos2], array[pos1]

def insertion_sort(array, method):
    i = 1
    while i < len(array):
        key = array[i]
        j = 0
        while j < i:
            if (method and array[j] > key) or (not method and array[j] < key):
                key = array[j]
                swap_elements(array, i, j)
            j += 1
        i += 1

# https://stackoverflow.com/questions/18262306/quicksort-with-python
def quicksort(array, method):
    lower_array = []
    equal_array = []
    greater_array = []
    if len(array) > 1:
        pivot = array[0]
        for el in array:
            if el == pivot:
                equal_array.append(el)
            else:
                if method:
                    if el < pivot:
                        lower_array.append(el)
                    else:
                        greater_array.append(el)
                else:
                    if el > pivot:
                        lower_array.append(el)
                    else:
                        greater_array.append(el)

        return quicksort(lower_array, method) + equal_array + quicksort(greater_array, method)  
    else:  
        return array

a1 = [4, 6, 1, 8, 2]
insertion_sort(a1, True)
print(a1) # [1, 2, 4, 6, 8]
print(quicksort([4, 6, 1, 8, 2], True)) # [1, 2, 4, 6, 8]

a2 = [7, 6, 1, 9, 4]
insertion_sort(a2, False)
print(a2) # [9, 7, 6, 4, 1]
print(quicksort([7, 6, 1, 9, 4], False)) # [9, 7, 6, 4, 1]
        
        

        
