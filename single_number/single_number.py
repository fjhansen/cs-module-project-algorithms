'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''



##def single_number(arr):
##    spot_marker = 0
##    for x in range(spot_marker, len(arr)):
##        if arr[x] == arr[spot_marker]:
##            arr[spot_marker] = arr[x]=+1
##            arr.remove(x)

##def single_number(arr):
##    return [x for x in arr if arr.count(x) != 2]

def single_number(arr):

    for x in arr:
        if arr.count(x) != 2:
            return x


    
        
        


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    

    print(f"The odd-number-out is {single_number(arr)}")






