def left_rotate(d: int, arr: list):
    if d == 0:
        return arr
    return arr[d % len(arr) :] + arr[: d % len(arr)]


print(left_rotate(8, [1, 2, 3, 4, 5]))
