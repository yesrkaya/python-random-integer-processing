import random

n = int(input("Enter the number of elements (n): "))
initial_list = [random.randint(1, 5) for _ in range(n)]
print("Initial list:", initial_list)


multiplied_list = [x * 4 for x in initial_list]
print("List after multiplying by 4:", multiplied_list)

filtered_list = [x for x in multiplied_list if x > 10]

sum_of_elements = sum(filtered_list)
print("Sum of elements greater than 10:", sum_of_elements)
