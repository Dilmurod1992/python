def is_prime(n):
    if n < 2:
        return False  
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False  
    return True

print(is_prime(4))  
print(is_prime(7))  





def digit_sum(k):
    return sum(int(digit) for digit in str(k))


print(digit_sum(24))   
print(digit_sum(502))  






def print_powers_of_two(N):
    k = 1
    while (power := 2 ** k) <= N:
        print(power, end=' ')
        k += 1



print_powers_of_two(10)

