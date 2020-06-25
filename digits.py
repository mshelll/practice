# A Dynamic Programming based 
# Python3 implementation to count decodings 

# A Dynamic Programming based 
# function to count decodings 


# Excellet Funda is in a string if last digit is valid its count is valid for me
# If last 2 digits are valid its count need to be aggregated as well

def countDecodingDP(digits, n): 

    # A table to store results of subproblems 
    count = [0] * (n+1) 
    count[0] = 1

    if int(digits[0:2]) < 27:
        count[1] = 2
    else:
        count[1] = 1

    for i in range(2, len(digits)):
        count[i] = count[i-1]

        # import pdb 
        # pdb.set_trace()
        
        num = int(digits[i-1:i+1])

        if num < 27:
            count[i] += count[i-2]

        print("num :", num)
        print("count :", count)


        # # If the last digit is not 0, 
        # 		# then last digit must add to 
        # # the number of words 
        # if (digits[i-1] > '0'): 
        # 	count[i] = count[i-1] 

        # # If second last digit is smaller 
        # 		# than 2 and last digit is 
        # # smaller than 7, then last two 
        # 		# digits form a valid character 
        # import pdb 
        # pdb.set_trace()
        # if (digits[i-2] == '1' or (digits[i-2] == '2' and digits[i-1] < '7') ): 
        # 	count[i] += count[i-2] 

        # print("i :", i, "digit :", digits[i-1], "count :", count[i])
    
    return count[len(digits)-1] 


# Driver program to test above function 
digits = ['1','9','3','4', '5'] 
#digits = ['1','9'] #,'3','4', '5'] 
n = len(digits) 

#print("Count is ",countDecodingDP(''.join(digits), n)) 

print("Count is ",countDecodingDP('1211', n)) 

# This code is contributed by 
# Smitha Dinesh Semwal 
