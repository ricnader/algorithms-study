
# A number from 1 to 10000

import time

def regularsearch(nRange,choice):
  start = time.time()
  
  for element in nRange:
    if (choice == element):
      print(f"choice is {choice}")                 
      return 
        
  print("Not found") 
  
  end = time.time()     
  print(f"elapsed time: {end - start}")



def binarySearch(nRange,choice):
  start = time.time()
  
  low = 0
  high = len(nRange)
  medium = round(len(nRange)/2)
  teste = nRange[medium]
  # for index, currentValue in enumerate(nRange):
          
  while(nRange[medium] != choice):    
    if(choice == nRange[medium]) or (high == low):
      print(f'the choice is {choice}')     
    elif(choice < nRange[medium]):
      high = medium
    elif(choice > nRange[medium]):
      low = medium
       
    medium = int(round(medium)/2)
  
  
  
  print(f'Not found')
  end = time.time()  
  print(f"elapsed time: {end - start}")



choice = int(input("Type the number you want to find:"))

input = input("type all the numbers you want include for search, separated by spaces:")

numbers = [int(number) for number in input.split()]

print(numbers)

print("Regular search")
regularsearch(numbers, choice)

print("Binary search")
binarySearch(numbers, choice)
