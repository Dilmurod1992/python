def insert_underscore(txt):
    vowels = 'aeiouAEIOU'
    result = []
    i = 0
    count = 0

    while i < len(txt):
        result.append(txt[i])
        count += 1

        if count == 3:
        
            j = i + 1
            while j < len(txt) and (txt[j] in vowels or txt[j] == '_'):
                j += 1
            if j < len(txt):
                result.append('_')
            count = 0
        i += 1

    if result and result[-1] == '_':
        result.pop()

    return ''.join(result)


print(insert_underscore("hello"))            
print(insert_underscore("assalom"))          
print(insert_underscore("abcabcabcdeabcdefabcdefg"))  




n = int(input())

for i in range(n):
    print(i ** 2)




i = 1

while i <= 10:
    print(i)
    i += 1




for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()




n = int(input("Enter a number: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Sum from 1 to", n, "is:", total)




num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num * i)




numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num > 500:
        break
    if num > 150:
        continue
    if num > 50:
        print(num)



num = int(input("Enter a number: "))
count = 0

while num != 0:
    num //= 10
    count += 1

print("Total digits:", count)






for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()



list1 = [10, 20, 30, 40, 50]

for i in range(len(list1) - 1, -1, -1):
    print(list1[i])





for i in range(-10, 0):
    print(i)




for i in range(5):
    print(i)
print("Done!")




start = 25
end = 50

print("Prime numbers between", start, "and", end, ":")

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)





n_terms = 10
a, b = 0, 1

print("Fibonacci sequence:")

for _ in range(n_terms):
    print(a, end='  ')
    a, b = b, a + b




num = int(input("Enter a number: "))
factorial = 1

if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("0! = 1")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"{num}! = {factorial}")





from collections import Counter

def uncommon_elements(list1, list2):
    c1 = Counter(list1)
    c2 = Counter(list2)
    
    result = []

    for elem in c1:
        if elem not in c2:
            result.extend([elem] * c1[elem])
        elif c1[elem] > c2[elem]:
            result.extend([elem] * (c1[elem] - c2[elem]))

    for elem in c2:
        if elem not in c1:
            result.extend([elem] * c2[elem])
        elif c2[elem] > c1[elem]:
            result.extend([elem] * (c2[elem] - c1[elem]))

    return result




print(uncommon_elements([1, 1, 2], [2, 3, 4]))           

print(uncommon_elements([1, 2, 3], [4, 5, 6]))           

print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))


