count = int(input("Enter the number of elements in the tuple: "))
sum = 0
test_list = []
for i in range(count):
    x = int(input("Enter the element: "))
    test_list.append(x)
test_tuple = tuple(test_list)
print(test_tuple)
for i in test_tuple:
    sum = sum + i
print("Sum of all the elements in the tuple is: ", sum)