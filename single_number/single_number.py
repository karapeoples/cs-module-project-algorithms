'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    #!SEARCH (Find Single Number in an array of duplicates of duplicates python) found this formula which seems to be a constant time solution.
    return 2*sum(set(arr)) - sum(arr)


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")