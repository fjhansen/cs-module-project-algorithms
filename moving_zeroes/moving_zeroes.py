# next time this task should be way more clear. "moving zeros" could mean 100 different things.
# should be "moving zeros to the end of the list". come on now!!!!

'''
Input: a List of integers
Returns: a List of integers

'''

def moving_zeroes(arr):
    new_list = []
    pop_count=+1

    for x in range(len(arr)):
        if arr[x] == 0:
            y = arr[x]
            arr.remove(arr[x])
            arr.insert((len(arr)+1), y)
    return arr


##def moving_zeroes(arr):
    # Your code here
##    new_list = []
##
##    for x in arr:
##        if x != 0 and x not in new_list:
##            new_list.append(x)
##    return new_list


# for [3, 1]:
##def moving_zeroes(arr):
##    new_list = []
##    pop_count = 0
##
##    for x in arr:
##        if arr[x-pop_count] and x not in new_list:
##            new_list.append(arr.pop(x-pop_count))
##            pop_count=+1
##    return new_list    

    


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
