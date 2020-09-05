# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 16:25:26 2020

@author: INPRDHI
"""
import os.path  as path

def strictly_increasing(arr):
    return all(x<y for x, y in zip(arr, arr[1:]))

def strictly_decreasing(arr):
    return all(x>y for x, y in zip(arr, arr[1:]))

# Python program of above implementation 
def getMinMax(low, high, arr):    
    
    arr_max = arr[low] 
    arr_min = arr[low] 
    
    # print(arr_max, arr_min,arr)
      
    # If there is only one element  
    # if low == high: 
    #     print("when equal")
    #     arr_max = arr[low] 
    #     arr_min = arr[low] 
    #     return (arr_min,arr_max) 
          
    strict_increase = strictly_increasing(arr)
    # print(strict_increase)
    strict_decrease = strictly_decreasing(arr)
    
    # If there is only two element 
    if high == low + 1: 
        if (strict_decrease): 
            arr_max = arr[low] 
            arr_min = arr[high] 
            # print("dec")
            return ("decreasing", arr_min,arr_max)
        if (strict_increase): 
            arr_max = arr[high] 
            arr_min = arr[low] 
            # print("inc")
            return ("increasing", arr_min,arr_max) 
        else:
            if(arr[low] < arr[high]):
                arr_max = arr[high] 
                arr_min = arr[low] 
                return ("maxima", arr_min,arr_max) 
            else:
                 arr_max = arr[low] 
                 arr_min = arr[high]
                 return ("minima", arr_min,arr_max)  
                
    else: 
          
        # If there are more than 2 elements 
        mid = int((low + high) / 2) 
        maxMin1, arr_min1, arr_max1 = getMinMax(low, mid, arr) 
        
        maxMin2, arr_min2, arr_max2 = getMinMax(mid + 1, high, arr) 
       
    # print(maxMin1, ":",arr_min1,":",arr_max1)
    # print(maxMin2, ":",arr_min2,":",arr_max2)
    
    if(maxMin1 == maxMin2):
         return (maxMin1, min(arr_min1, arr_min2),max(arr_max1, arr_max2) )
     
    elif(maxMin1 == "decreasing" or maxMin1 == "minima"):
        return("minima", min(arr_min1, arr_min2), max(arr_max1, arr_max2))
    else: 
        return("maxima", min(arr_min1, arr_min2), max(arr_max1, arr_max2))
      
  
   # return (max(arr_max1, arr_max2), min(arr_min1, arr_min2)) 
  
# Driver code 
# arr = [1000, 11, 445, 1, 330, 3000] 
# high = len(arr) - 1
# low = 0
# arr_max, arr_min = getMinMax(low, high, arr) 
# print('Minimum element is ', arr_min) 
# print('nMaximum element is ', arr_max) 
  

#####
inputFile,outputFile="inputPS4.txt","outputPS4.txt"
file_write = open(outputFile, 'w')
if (path.exists(inputFile)):
    file_obj = open(inputFile, "r") 
    for get_line in file_obj.readlines():
        # curr_line_arr = get_line.rstrip().split(" ")
        curr_line_arr = [int(i) for i in get_line.rstrip().split(" ")] 
        print(curr_line_arr)
        high = len(curr_line_arr) - 1
        low = 0
        maxMin, arr_min, arr_max = getMinMax(low, high, curr_line_arr) 
      
        print(maxMin)
        print(arr_min)  
        print(arr_max) 
               
        
        if(maxMin == "increasing" or maxMin == "decreasing"):
            fileContent = str(maxMin)+" "+ str(arr_min) + "\n"
            file_write.write(fileContent)
            
        elif(maxMin == "minima"):
            fileContent = str(maxMin)+" "+ str(arr_min)+ "\n"
            file_write.write(fileContent)
        
        else: 
            fileContent = str(maxMin) + " "+ str(arr_max)+ "\n"
            file_write.write(fileContent)
            
file_obj.close()
file_write.close()
      