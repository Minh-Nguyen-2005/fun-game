#Author: Minh Nguyen
#Date: 10/17/2023
#Purpose: Counter class

#a counter that counts down. When it gets down to 0 and counts down again,
# it wraps back to a limit, minus 1. For example, if the limit is 60,
# the counter's value is 0, and it counts down, its next value is 59.
class Counter:
    def __init__(self, limit, initial = 0, min_digits = 1):
        self.limit = limit
        self.min_digits = min_digits
        if initial >= 0 and initial <= limit - 1:
        #If the initial value supplied as a parameter is between 0 and limit–1,
        #then that's the counter's initial value.
            self.initial = initial
        else: #Otherwise, an error message is printed and the counter's initial value is limit–1.
            print("Error")
            self.initial = limit - 1

    def get_value(self): #returns the counter's value, as an int.
        return int(self.initial)

    def __str__(self): #returns the counter's value, as a string.
    #If the counter's value would print with fewer than the min_digits parameter
    # supplied to the __init__ method, then the string contains min_digits characters,
    # padded on the left with zeros.
        if len(str(self.initial)) < self.min_digits:
            return "0" * (self.min_digits - len(str(self.initial))) + str(self.initial)
        else:
            return str(self.initial)

    def tick(self): #decrements the counter's value
        if self.initial - 1 < 0: #if the value would go negative, then it becomes limit–1.
            self.initial = self.limit - 1
            return True #means that it wrapped.
        else:
            self.initial = self.initial - 1
        return False #means that it did not wrap.
