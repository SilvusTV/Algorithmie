def recherche_lineaire(data, conditional_function):
    comp = 0
    results = []

    for line in data:
        comp += 1
        if conditional_function(line):
            results.append(line)

    return results, comp

def recherche_binaire(array, target):
    left = 0
    right = len(array) - 1
    comp = 0

    while left <= right:
        middle = (left + right) // 2
        comp += 1
        if array[middle] == target:
            return middle, comp
        elif array[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1, comp

def recherche_min_max(array):
    if not array:
        return None, None, 0

    min_value = max_value = array[0]
    comp = 0

    for value in array[1:]:
        comp += 1
        if value < min_value:
            min_value = value
        comp += 1
        if value > max_value:
            max_value = value

    return min_value, max_value, comp
