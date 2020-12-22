def center_zeros(array,n):
   
    new = []
    zeros = []
   
    
    for i in range(len(array)):
        if array[i] == 0 or array[i] == 0.0:
            if type(array[i]) == int or type(array[i]) == float:
                zeros.append(array[i])
            else: new.append(array[i])
        else:
            new.append(array[i])
    mylist = new[:n]+zeros+new[n:]
    return mylist
        
def middle_element(list):
  middle=0
  if int(len(list))<2:
    middle = 1  # if it has less than 2 entries, the first entry is the middle one. 
  elif int(len(list)) %2 == 0 :
    middle = int(len(list)/2)
  else: 
    middle = int((len(list)/2) - 1)
  return middle-1  

if __name__ == "__main__":
    # write your debug code here
   # Driver code 
#center_zeros([1, 1, 3, 0, 6, 0]) -> [1, 1, 0, 0, 3, 6]
    arr2 = [1, 1, 3, 0, 6, 0] 
    m = middle_element(arr2)
    print(center_zeros(arr2,m))


