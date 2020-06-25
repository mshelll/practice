
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.




# Algorithm



Traverse array Create a stack

Appe nd elemene to stack if greater than top 


else : 
    
    Pop element find the profit bu=y selling at that day 
    Match again current max
    
    
    
    
 
def stock_predict(arr):

    if len(arr) == 0 :
        return 0
        
    n = len(arr)
    
    
    max_elem = 0
        
    for i in range(n):
        for j in range(i, n):
            diff == arr[j] - arr[i]
            if diff > 0:
                 max_elm = max(arr[j] - arr[i], max_elem)
            
      
      
def stock_predict(arr):

    if len(arr) == 0 :
        return 0
        
    n = len(arr)
    
    
    max_elem = 0
        
    for i in range(n):
        for j in range(i, n):
            diff == arr[j] - arr[i]
            if diff > 0:
                 max_elm = max(arr[j] - arr[i], max_elem)
                 
                 
                 
 
 
bank_balance = 0


mux = threading.Mutex()
 
 
def deposit(amount):

    mux.lock()
    
    balance += amount
    mux.unlock()

   

def withdraw(amount):
    mux.lock()
    
    balance -= amount
    mux.unlock()


def customer():

    sleep(5)
    deposit(5)
    sleep(5)
    withdraw(3)

def main():

    cust_a = threading.Thread(target=customer)
    cust_b = threading.Thread(target=customer)
    
    
     cust_a.join()
     cust_b.join()

    
            
            
         
            
