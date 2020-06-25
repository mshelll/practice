"""
Given a sorted array of n elements, possibly with duplicates, find the number of occurrences of the target element.

Example 1:

Input: arr = [4, 4, 8, 8, 8, 15, 16, 23, 23, 42], target = 8
Output: 3

Example 2:

Input: arr = [3, 5, 5, 5, 5, 7, 8, 8], target = 6
Output: 0

"""


def find_occurence(arr, target):
    
    count = 0
    for elem in arr:
        if elem == target:
            count += 1
            
    return count
    
    
def find_occurence(arr, target):
    
    count = 0
    
    high = len(arr) -1
    low = 0
    
    found = -1
    
    while(low < high):
    
        if arr[low] == arr[high] == target:
            return high - low
        
        mid = (low + high) // 2
        
        //if arr[mid] == target:
            //high = mid
          
        elif arr[mid] > target:
            high = mid-1
        elif arr[mid] < target:
            low = mid+1
            
            
    return 0
    
    
    
    
    def find(arr, low, high, target):
    
        mid = low + high / 2
        
        count1 = find(arr, low, mid-1, target)
        count2 = find(arr, mid+1, high, target)
        
        if arr[mid] == target:
            found = 1
            
        return count1 + count2 + found
        
        
            
        
               
    // found = 3   
    count = 0            
    if found:
        
        
        i = found
        while(a[i] == target):
            count += 1
            i += 1
            
        j = found
        while(a[j] == target):
            count += 1
            j -= 1
            
            
     return count+1
            
            
 
    
    Marshel: trying to connect to toll free number
    
    Can you wait 1 min  ?
    
    
    [3, 5, 5, 5, 5, 7, 8, 8]
    
    
    mid = 3
    
    elem = 5
    
    
    found = 3
    
    Traverse left and right of 3 , keep count of elem found as target 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
