# Operates on the FIFO protocol
# Can be circular or linear
# Operations: Push, Pop and Peak (to get the element on the top of the stack)
# Pointers: Front pointer (points to the first location), Rear pointer (points to the last element in the queue)

#Declare the queue as an array (it has a fixed length)

Queue = [None for i in range(7)]
frontPointer = 0
rearPointer = -1
Queuefull = len(Queue)
QueueLength = 0 


def Enqueue(enqueueele):
    global QueueLength, rearPointer
    if QueueLength < Queuefull: # Checks whether the queue is full
        if rearPointer == Queuefull - 1: # The queue is not full so there is still space to enqueue but the last element is at the end of the queue
            rearPointer = 0 # Rear pointer points to the first space of the queue again
        else:
            rearPointer += 1
        Queue[rearPointer] = enqueueele
        QueueLength += 1
    else:
        print("Unable to enqueue, Queue is full.")


def Dequeue():
    global QueueLength, frontPointer
    if QueueLength > 0: # Checks whether the queue has items in it
        dequeueele = Queue[frontPointer]
        if frontPointer == Queuefull - 1:
            frontPointer = 0
        else:
            frontPointer += 1
        QueueLength -= 1
        return dequeueele
    else:
        print("Unable to dequeue, queue is empty.")

# Enqueue(1)
# print(Queue)
# Enqueue(7)
# print(Queue)
# print(Dequeue())


