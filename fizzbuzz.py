
result = ["fizzbuzz" if i % 15 == 0 else "fizz" if i % 3 == 0 else "buzz" if i % 5 == 0 else i for i in range(16, 31)]


print(*result, sep="\n")
