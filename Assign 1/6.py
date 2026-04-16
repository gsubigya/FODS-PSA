#check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

#user input
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

primes = []
total_sum = 0

# Find prime numbers in range
for num in range(start, end + 1):
    if is_prime(num):
        primes.append(num)
        total_sum += num

# Display results
print(primes)
print(f"Count of prime numbers: {len(primes)}")
print(f"Sum of prime numbers: {total_sum}")