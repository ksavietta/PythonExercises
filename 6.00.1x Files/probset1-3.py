s = 'azcbobobegghakl'


result_string = s[0]
alpha_bit = s[0]

for i, letter in enumerate(s):
    if i == len(s)-1:
        break
    elif letter <= s[i+1]:
        alpha_bit += s[i+1]  
        print alpha_bit  
    else:
        alpha_bit = s[i+1]
    if len(alpha_bit) > len(result_string):
        result_string = alpha_bit
        
print "Longest substring in alphabetical order is: {}".format(result_string)