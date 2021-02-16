from math import ceil


def center_zeros(array):
    # write your function here
    # center means the floor(x / 2) where floor means rounding a float (decimal number) down to the nearest integer
    # i.e. floor(1) = 1, floor(1.5) = 1, floor(1.75) = 1, floor(2) = 2

    #variable
    count = 0

    if array:
        # Get count of Zero in an array
        for number in array:
            if number == 0:
                count += 1
                array.pop(array.index(number))
            
        # split by median
        center_num = ceil(len(array)/2)
        array_left = array[:center_num]
        array_right = array[center_num:]

        #append 0 to middle
        for x in range(count):
            array_left.append(0)

        #join both arrays
        new_array = array_left + array_right

        return new_array
    else:
        return array


if __name__ == "__main__":
    # write your debug code here
    print(center_zeros([0, 3, 1]))
    print(center_zeros([1, 1, 3, 0]))
    print(center_zeros([1, 1, 3, 0, 6, 0]))
    print(center_zeros([0, 0, 1]))
    print(center_zeros([]))