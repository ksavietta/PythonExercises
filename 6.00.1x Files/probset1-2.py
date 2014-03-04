
def find_num_bob(s, pattern):
    num_bob = 0
    start = 0
    while True:
        start = s.find(pattern, start) + 1
        if start > 0:
            num_bob +=1
        else: 
            return num_bob    

num_bob = find_num_bob('azcbobobegghakl','bob')
print "Number of times bob occurs is: {}".format(num_bob)