def select_max(array):
    # write your function here
    # do NOT use the built-in max() function
    array.sort()
    if not array:
        return None
    return array.pop()
       


if __name__ == "__main__":
    # write your debug code here
    print(select_max([1, 2, 3]))
    print(select_max([0]))
    print(select_max([0, 0, 0]))
    print(select_max([-10, -2, -8]))
    print(select_max([-10, -2, 1]))
    print(select_max([]))
