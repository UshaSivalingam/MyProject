'''Given a list, write a Python program to swap first and last element of the list.

Examples: 

Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]

Input : [1, 2, 3]
Output : [3, 2, 1]'''

def swap(new_list):
    new_list[0], new_list[-1] = new_list[-1], new_list[0]
    return new_list

a = list(map(int, input("enter an array of list:").split()))
print("output after interchanging first and last element is:",swap(a))