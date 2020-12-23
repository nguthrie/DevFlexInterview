def center_zeros(array):
   
    new = []
    zeros = []
    n=middle_element(array)
   
    
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
  assert center_zeros([0, 3, 1]) == [3, 0, 1]
  print(center_zeros([0, 3, 1]))


