def tri_selection(tab):
    array = tab[:]
    n = len(array)
    comp = 0
    flip = 0

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            comp += 1
            if array[j] < array[min_index]:
                min_index = j
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]
            flip += 1

    return array, comp, flip

def tri_insertion(tab):
    array = tab[:]
    n = len(array)
    comp = 0
    gap = 0

    for i in range(1, n):
        cle = array[i]
        j = i - 1
        while j >= 0:
            comp += 1
            if array[j] > cle:
                array[j + 1] = array[j]
                gap += 1
                j -= 1
            else:
                break
        array[j + 1] = cle

    return array, comp, gap

def tri_fusion(tab):
    comp = [0]

    def fusion(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            comp[0] += 1
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def fusion_rec(liste):
        if len(liste) <= 1:
            return liste
        mid = len(liste) // 2
        left = fusion_rec(liste[:mid])
        right = fusion_rec(liste[mid:])
        return fusion(left, right)

    sorted_tab = fusion_rec(tab[:])
    return sorted_tab, comp[0]

def tri_rapide(tab):
    comp = [0]
    exchanges = [0]

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            comp[0] += 1
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                exchanges[0] += 1
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        exchanges[0] += 1
        return i + 1

    def quicksort(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quicksort(arr, low, pi - 1)
            quicksort(arr, pi + 1, high)

    array = tab[:]
    quicksort(array, 0, len(array) - 1)
    return array, comp[0], exchanges[0]
