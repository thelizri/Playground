def merge(arrayOne, arrayTwo):
    result = []
    while len(arrayOne) > 0 and len(arrayTwo) > 0:
        if arrayOne[0] > arrayTwo[0]:
            result.append(arrayTwo[0])
            arrayTwo.pop(0)
        else:
            result.append(arrayOne[0])
            arrayOne.pop(0)

    while len(arrayOne) > 0:
        result.append(arrayOne[0])
        arrayOne.pop(0)

    while len(arrayTwo) > 0:
        result.append(arrayTwo[0])
        arrayTwo.pop(0)

    return result


def mergesort(array):
    length = len(array)
    if length == 1:
        return array

    min, mid, max = 0, length // 2, length

    arrayOne = array[min:mid]
    arrayTwo = array[mid : max + 1]

    arrayOne = mergesort(arrayOne)
    arrayTwo = mergesort(arrayTwo)

    return merge(arrayOne, arrayTwo)


testArray = [2, 8, 5, 3, 9, 4, 1, 7]
print(mergesort(testArray.copy()))
testArray.sort()
print(testArray)
