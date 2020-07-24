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

##def product_of_all_other_numbers(arr):
##    new_list = []
##    current_num = 0
##
##    for x in range(current_num, len(arr)+1):
##        print(f'\nx: {arr[current_num]} {arr[x]}\n')
##        
##        for y in range(current_num,len(arr)+1):
##            print(f'y: {arr[current_num]} {arr[y]}')

def product_of_all_other_numbers(arr):
    
    product_of_all_except_at_index = [None] * len(arr)
    
    print(f'product_of_all_except_at_index: {product_of_all_except_at_index}')
    product = 1
    for i in range(len(arr)):
        product_of_all_except_at_index[i] = product
        print(f'1. A: {product}')
        print(f'2. B: {arr[i]}')
        product *= arr[i]
        print(f'3. A *= B: {arr[i]}')
        print(f'4: {product_of_all_except_at_index} \n')

    product = 1
    # this makes it possible to go through the list backwards by reversing the indices.
    # makes it possible to avoid using another O(n)
    for i in range(len(arr) -1, -1, -1):
        print(f'5. C: {product_of_all_except_at_index[i]}')
        print(f'6. D: {product}')
        product_of_all_except_at_index[i] *= product
        print(f'7. C *= D: {product}')

        print(f'8. E: {product}')
        print(f'9. F: {arr[i]}')
        
        product *= arr[i]

        print(f'10. E *= F: {arr[i]}')

        print(f'11: {product_of_all_except_at_index} \n')

    return product_of_all_except_at_index
    

    






if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [9,90]
    #arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
