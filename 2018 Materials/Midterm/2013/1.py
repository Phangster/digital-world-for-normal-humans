input_numbers = raw_input("Enter integers n1 and n2: ")
number_list = input_numbers.split(' ')
n1, n2 = int(number_list[0]), int(number_list[1])
print [i for i in range(n1, n2 + 1) if i % 2 != 0]

