#print "Hello"



# Your last C/C++ code is saved below:
# #include <iostream>
# using namespace std;

# int main() {
# 	cout<<"Hello";
# 	return 0;
# }


class Node:
   def __init__(self, id, val):
     self.id = id
     self.val = val

class Cache:
    def __init__(self, size):
      self.queue = []
      self.lookup = {}
      self.size = size
      
    def full(self):
      return len(self.queue) == self.size
      
    def empty(self):
      return len(self.queue) == 0
      
    # O(1)
    def get(self, id):
      if self.empty(): #or id not in self.lookup.keys():
        return "Err not found"
      try:
        return self.lookup[id].val
      except: 
        return "Err not found"
      #return self.lookup[id].val
       
    # best case O(1)   Worst Case : )(n)
    def put(self, id, val):
  
      if id in self.lookup:
        print("elem found :", id)
        node = self.lookup[id]
        node.val = val
        return

      if self.full():
          #del_id = self.queue.front().id
          elem = self.queue.pop(0).id
          del self.lookup[elem]
          print("popped elem :", elem)
          
      node = Node(id, val)
      self.queue.append(node)
      self.lookup[id] = node
      
    def dumpq(self):
      for node in self.queue:
        print("{} : {}".format(node.id, node.val))
      



def main():
  
   print "----Start"
   cache = Cache(5)
   
   #cache.get(1)  # Err empty
   
   cache.put(1, 6)
   #print("get 1 :", cache.get(1))  # shud work
   
   for i in range(5):
     cache.put(i, 3)
     
   cache.dumpq()
     
   cache.put(3, 7)  # Err Full
   
   cache.dumpq()
   print "---End"
   
   
   
if __name__ == "__main__":
   main()