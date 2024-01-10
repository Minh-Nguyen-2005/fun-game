#Author: Minh Nguyen
#Date: 10/17/2023
#Purpose: Counter driver

from counter import Counter

#create three Counter objects and demonstrate that all the methods
# in the Counter class work properly by printing to the console.

print("-------------wrapped1")
count1 = Counter(60, 18, 2)
wrapped1 = False
while wrapped1 is False:
    print(count1.get_value())
    print(count1)
    wrapped1 = count1.tick()
    print(wrapped1)

print("-------------wrapped2")
count2 = Counter(60, 2, 2)

print(count2.get_value())
print(count2)
wrapped2 = count2.tick()
print(wrapped2)

print(count2.get_value())
print(count2)
wrapped2 = count2.tick()
print(wrapped2)

print(count2.get_value())
print(count2)
wrapped2 = count2.tick()
print(wrapped2)

print(count2.get_value())
print(count2)
wrapped2 = count2.tick()
print(wrapped2)

print("-------------wrapped3")
count3 = Counter(60, 60, 2)
wrapped3 = False
while wrapped3 is False:
    print(count3.get_value())
    print(count3)
    wrapped3 = count3.tick()
    print(wrapped3)