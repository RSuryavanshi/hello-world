#import sum from hello_world
#import hello_world
import sys
#sys.path.append('../')
from hello_world import sum

print "############# Unit Test Script"

print "############# Test case 1"
total = sum(3, 4)
print "Total:", total


print "############# Test case 2"
total = sum(10, 4)
print "Total:", total