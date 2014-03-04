s = 'azcbobobegghakl'

num_bob = 0
start = 0
while True:
    start = s.find('bob', start) + 1
    if start > 0:
        num_bob +=1
    else: 
        break   

print "Number of times bob occurs is: {}".format(num_bob)