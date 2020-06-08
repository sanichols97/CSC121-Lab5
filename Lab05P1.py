integers = []
yes_no = "y"
while yes_no == "y":
    new_int = int(input("Enter an integer from 1 to 10: "))
    integers.append(new_int)
    yes_no = input("Would you like to enter another integer? [y/n]")
    yes_no = yes_no.lower()
print("\nNumber list: ", integers)
print("Largest element: ", max(integers))
print("Smallest element: ", min(integers))
print("Sum of all elements: ", sum(integers))
print("Length of list: ", len(integers))
average = sum(integers) / len(integers)
print("Average of list: ", average)
integers.reverse()
print("Reversed order: ", integers)
integers.insert(0, integers[-1])
del integers[-1]
print("Last element moved to front: ", integers)
