
# A number from 1 to 10000

import time

def regularsearch(nRange,choice):
  start = time.time()
  
  for element in nRange:
    if (choice == element):
      print(f"choice is {choice}")
      end = time.time()      
      print(f"elapsed time: {end - start}")
      return 
        
  print("Not found")     





def binarySearch(nRange,choice):
  start = time.time()
  
  low = 0
  high = len(nRange)
  medium = len(nRange)/2
  
  while(choice != medium):    
    if(choice == medium):
      return f"The choice is{choice}"
    elif(choice < medium):
       high = medium
    elif(choice > medium):
       low = medium

    medium = round(medium /2)
    end = time.time()  
    
  print(f"elapsed time: {end - start}")




choice = int(input("Type the number you want to find:"))

input = input("type all the numbers you want include for search, separated by spaces:")

print("Regular search")
regularsearch(input, choice)

print("Binary search")
binarySearch(input, choice)
