#Author: Minh Nguyen
#Date: 10/17/2023
#Purpose: Timer class

from counter import Counter

#a 24-hour hours:minutes:seconds timer that counts down.
#instance variables that reference Counter objects for the hours, minutes, and seconds.
class Timer:
    def __init__(self, hours, minutes, seconds):
    #create three Counter objects and save the references given back by the
    # Counter constructors in instance variables for the Timer object.
        self.hours = Counter(24, hours, 2)
        self.minutes = Counter(60, minutes, 2)
        self.seconds = Counter(60, seconds, 2)

    def __str__(self): #returns a string giving the timer's current time, in the format hh:mm:ss.
        return str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds)

    def tick(self): #ticks down the timer by one second.
        if self.seconds.tick():
            if self.minutes.tick():
                self.hours.tick()

    def is_zero(self): #returns a boolean that is True if the timer currently reads 00:00:00.
        if self.hours.get_value() == 0 and self.minutes.get_value() == 0 and self.seconds.get_value() == 0:
            return True
        return False