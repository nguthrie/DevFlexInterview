def minPoint(arr, l, h):
 
    # Base case: when source and
    # destination are same
    if (h == l):
        return 0
 
    # when nothing is reachable 
    # from the given source
    if (arr[l] == 0):
        return len(arr)
 
    # Traverse through all the points 
    # reachable from arr[l]. Recursively 
    # get the minimum number of jumps 
    # needed to reach arr[h] from 
    # these reachable points.
    min = float('inf')
    for i in range(l + 1, h + 1):
        if (i < l + arr[l] + 1):
          jumps = minPoint(arr, i, h)
          if (jumps != float('inf') and
            jumps + 1 < min):
             min = jumps + 1
 
    return min


if __name__ == "__main__":
    # write your debug code here
    arr =[1, 2, 3]
    n = len(arr)
    arr2=[1, 2, 3, 5, 8]
    m = len(arr2)
    print('Minimum points',
     'is', minPoint(arr,0, n-1))
    print('Minimum points',
     'is', minPoint(arr2,0, m-1))
    arr3 =[1,2,3,4,5]
    y = len(arr2)
    print('Minimum points',
     'is', minPoint(arr3,0, y-1))