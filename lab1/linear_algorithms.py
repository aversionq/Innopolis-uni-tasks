# from math import prod
# print(str(sum(list(map(int, list(str(number := int(input("Input int number: "))))))))
#     + "\n" + str(prod(list(map(int, list(str(number)))))))

num = int(input())
last = num % 10
mid = num // 10 % 10
start = num // 100
print(last + mid + start)
print(last * mid * start)
