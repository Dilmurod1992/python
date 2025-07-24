def is_leap_year(year):
   
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(is_leap_year(2024))  
print(is_leap_year(1900))  
print(is_leap_year(2000))  




n = int(input("Enter a positive integer (1 to 100): "))

if n < 1 or n > 100:
    print("Invalid input. n must be between 1 and 100.")
else:
    
    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:  
        print("Not Weird")




a = int(input("Enter a: "))
b = int(input("Enter b: "))

if a <= b:
    even_numbers = list(range(a + (a % 2), b + 1, 2))
else:
    even_numbers = list(range(a - (a % 2), b - 1, -2))

print("Even numbers:", even_numbers)




a = int(input("Enter a: "))
b = int(input("Enter b: "))

start, end = sorted((a, b))

even_start = start + (start % 2)

even_numbers = list(range(even_start, end + 1, 2))

even_numbers = even_numbers[::-1] if a > b else even_numbers

print("Even numbers:", even_numbers)
