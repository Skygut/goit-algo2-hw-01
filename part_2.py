import random


def quick_select(arr, k):

    if len(arr) == 1:
        return arr[0]

    pivot = random.choice(arr)

    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    if k <= len(less):
        return quick_select(less, k)
    elif k <= len(less) + len(equal):
        return pivot
    else:
        return quick_select(greater, k - len(less) - len(equal))


if __name__ == "__main__":
    array = [7, 10, 4, 3, 20, 15]
    k = 4
    result = quick_select(array, k)
    print(f"{k}-й найменший елемент: {result}")
