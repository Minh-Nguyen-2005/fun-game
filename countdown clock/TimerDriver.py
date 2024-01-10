#Author: Minh Nguyen
#Date: 10/17/2023
#Purpose: Timer driver

from timer import Timer

#start a timer at 01:30:00 and count it down to 00:00:00,
# printing to the console all the times between and including 01:30:00 and 00:00:00.

count = Timer(1, 30, 0)

check_zero = False
while check_zero is False:
    check_zero = count.is_zero()
    print(count)
    count.tick()