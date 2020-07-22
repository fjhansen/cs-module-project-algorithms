'''
Input: a List of integers
Returns: a List of integers
'''
##def product_of_all_other_numbers(arr):
##    # Your code here
##    new_list = []
##
##    for x in range(len(arr)):
##        print(f'x: {x}')
##        for y in range(len(arr)=+1):
##            print(f'y: {y}, x*y: {x*y}')
##
##    return new_list

def product_of_all_other_numbers(arr):
    new_list = []
    current_num = 0

    for x in range(current_num, len(arr)+1):
        print(f'\nx: {arr[current_num]} {arr[x]}\n')
        
        for y in range(current_num,len(arr)+1):
            print(f'y: {arr[current_num]} {arr[y]}')

           

            

            
        

    return new_list






if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    #arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
