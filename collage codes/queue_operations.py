# class CircularQueue:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.queue = [None] * capacity
#         self.front = 0
#         self.rear = -1
#         self.size = 0
#     def enQueue(self, value):
#         if self.isFull():
#             return False
#         self.rear = (self.rear + 1) % self.capacity
#         self.queue[self.rear] = value
#         self.size += 1
#         return True

#     def deQueue(self):
#         if self.isEmpty():
#             return False
#         self.front = (self.front + 1) % self.capacity
#         self.size -= 1
#         return True

#     def Front(self):
#         if self.isEmpty():
#             return -1
#         return self.queue[self.front]

#     def Rear(self):
#         if self.isEmpty():
#             return -1
#         return self.queue[self.rear]

#     def isEmpty(self):
#         return self.size == 0

#     def isFull(self):
#         return self.size == self.capacity

# #  main method starts fromm 
# cq = CircularQueue(5)

#     # Perform operations and print results
# print("Enqueue 10:", cq.enQueue(10))  # Should return True
# print("Enqueue 20:", cq.enQueue(20))  # Should return True
# print("Enqueue 30:", cq.enQueue(30))  # Should return True
# print("Enqueue 40:", cq.enQueue(40))  # Should return True
# print("Enqueue 50:", cq.enQueue(50))  # Should return True
# print("Enqueue 60:", cq.enQueue(60))  # Should return False (queue is full)

# print("Front element:", cq.Front())  # Should return 10
# print("Rear element:", cq.Rear())    # Should return 50

# print("Dequeue:", cq.deQueue())  # Should return True
# print("Dequeue:", cq.deQueue())  # Should return True

# print("Enqueue 60:", cq.enQueue(60))  # Should return True
# print("Front element:", cq.Front())  # Should return 30
# print("Rear element:", cq.Rear())    # Should return 60

# print("Is queue empty:", cq.isEmpty())  # Should return False
# print("Is queue full:", cq.isFull())    # Should return True








class queue :
    def __init__(self,capacity):
        self.capacity = capacity
        self.front  = 0
        self.rear = -1
        self.size = 0
        self.queue = [None]*capacity
        
    def enqueue (self,value):
        if self.isfull():
            print ("you can not add element in the queue because it is full")
            return False
        self.rear = (self.rear+1)%self.capacity
        self.queue[self.rear]= value
        print ("added")
        self.size+=1
        return True
    def dequeue (self):
        if  self.isempty() :
            print ('you cant remove element from your queue because it is empty')
            return False
        
        print ('removed')
        self.front = (self.front+1)%self.capacity
        self.size -=1
        return True
    def isempty (self):
        return self.size == 0
          
    def isfull (self):
        return self.capacity==self.size
    def get_rear (self):
        return self.queue[self.rear]
    def get_front (self):
        return self.queue[self.front]
q1 = queue(5)
q1.enqueue (4)  
q1.enqueue (4)
q1.enqueue (5)
q1.enqueue (6)
q1.enqueue (7)
q1.enqueue (8)
q1.enqueue (7)
q1.dequeue()
q1.dequeue()
q1.dequeue()
q1.dequeue()
print (q1.isempty())
print (q1.isfull())
print (q1.get_front())
print (q1.get_rear())        
