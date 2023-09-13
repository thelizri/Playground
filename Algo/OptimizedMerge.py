def merge(array, aux, min, mid, max):
    posOne, posTwo, auxPos = min, mid, min

    # Copy the relevant segment of the original array into the auxiliary array
    for i in range(min, max):
        aux[i] = array[i]

    while posOne < mid and posTwo < max:
        if aux[posOne] > aux[posTwo]:
            array[auxPos] = aux[posTwo]
            posTwo += 1
        else:
            array[auxPos] = aux[posOne]
            posOne += 1
        auxPos += 1

    # ArrayOne or ArrayTwo should be empty by now
    while posOne < mid:
        array[auxPos] = aux[posOne]
        posOne += 1
        auxPos += 1

    while posTwo < max:
        array[auxPos] = aux[posTwo]
        posTwo += 1
        auxPos += 1


def mergesort(array, aux, min, max):
    length = max - min - 1
    if length <= 1:
        return

    mid = (min + max - 1) // 2

    # Sort each half
    mergesort(array, aux, min, mid)
    mergesort(array, aux, mid, max)

    # Merge the sorted halves
    merge(array, aux, min, mid, max)


testArray = [2, 8, 5, 3, 9, 4, 1, 7]
aux = [0 for _ in range(len(testArray))]
mergesort(testArray, aux, 0, len(testArray))
print(testArray)
