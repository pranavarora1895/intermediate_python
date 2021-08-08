import queue

q = queue.Queue()
s = queue.LifoQueue()
p = queue.PriorityQueue()
# 1,2,3,4,5
# 1
# 2,3,4,5
numbers = [10,20,30,40,50,60,70]

for number in numbers:
    q.put(number)
    s.put(number)
# print(q.full())
print(q.get())
print(q.get())
print(s.get())
# print(q.full())

p.put((5, "Pranav"))
p.put((2, "Arora"))
p.put((1, "Bindass!!"))

print(p.get()[1])