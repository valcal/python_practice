"""
Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.
"""

n = int(input("Enter a number to which Fibonacci sequence should be generated:"))
fibonacci_dict = [0, 1]
for number in range(0, n -1):
    fibonacci_dict.append(fibonacci_dict[-1] + fibonacci_dict[-2])
if n == 0:
    print(fibonacci_dict[0])
else:
    print(', '.join(map(str, fibonacci_dict)))
