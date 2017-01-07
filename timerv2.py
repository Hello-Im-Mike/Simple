'''This an attempt at a timer program that alerts the user when a certain amount
of time that they define has passed. It uses Python 2.7.

'''
# These are two built-in modules needed for the code to work.
import time
import os

# Here I am clearing the screen.
os.system ('clear')

# Here I greet the user and tell them what they are looking at.
print '''
------------------------------------------------------
Hello. Here you can set a timer.

The program will alert you after a chosen amount of time has passed.
------------------------------------------------------
'''



total_time = input ("How many seconds do you want the timer to run for? ")



for t in range(total_time):
    minutes = t / 60
    seconds = t % 60
    print "%d:%d" % (minutes,seconds) 
    time.sleep(1.0)
    
print "Game Over!"

