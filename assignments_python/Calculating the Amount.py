output = 0
    
left_max = 0
right_max = 0
input_numbers = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
n = len(input_numbers)

lo = 0
hi = n-1
    
while lo <= hi:
    
    if input_numbers[lo] < input_numbers[hi]:
        
        if input_numbers[lo] > left_max :

            left_max = input_numbers[lo]
        else:

            output += left_max - input_numbers[lo]
        lo+= 1
        
    else:
        
        if input_numbers[hi] > right_max :
            right_max = input_numbers[hi]
        else:
            output += right_max - input_numbers[hi]
        hi-= 1
        

print("Rain-trapped area:", output)
 