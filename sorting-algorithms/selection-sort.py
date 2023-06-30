def sort():
  arr = [10,5,2,1,4]
  newArr = []
  index = 0

  for i in range(0,len(arr)):
    index = searchSmaller(arr)
    newArr.append(arr[index])
    arr.pop(index)
  
  print(newArr)


def searchSmaller(arr):
  smaller_n = arr[0]
  smaller_i = 0
  
  for i in range(1,len(arr)): 
    if smaller_n < arr[i]:
      smaller_n = arr[i]
      smaller_i = i
      
  return smaller_i
      
     
      
sort()