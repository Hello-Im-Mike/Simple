#Countdown Timer

raw_input()

from time import sleep

for i in range(0,10):
    print 10 - i
    sleep(1)

for i in range(0,10):
    print 0 + i
    sleep(1)

print 'Blastoff!'