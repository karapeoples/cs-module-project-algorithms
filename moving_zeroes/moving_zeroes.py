'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    #!Search Query (move zeros to end of array python)
    count = 0
    for i in range(len(arr)):
        if arr[i]:
            temp = arr[i]
            arr[i] = arr[count]
            arr[count]= temp
            count += 1
    #!return is necessary for tests
    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")