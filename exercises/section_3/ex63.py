
numbers_str = input("Enter numbers separated by spaces: ")
numbers = [float(num) for num in numbers_str.split()]
 
print("Average of ", numbers, " is ", round(sum(numbers) / len(numbers), 3))

# summ = 0
# count = 0
# while True:
#     number = int(input('enter:  '))
#     summ += number
#     count += 1
#     if number == 0:
#         print(summ / (count - 1))
#         break
#     else:
#         continue    