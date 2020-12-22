def select_max(nums):
    # write your function here
    # do NOT use the built-in max() function
    maximum = None
    for num in nums:
        if maximum == None or num > maximum:
            maximum = num
    return maximum


if __name__ == "__main__":
    # write your debug code here
    print(select_max([1, 2, 3, 4]))
