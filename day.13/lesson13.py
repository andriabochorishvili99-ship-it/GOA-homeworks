n = int(input("Enter a positive integer: "))


count = 0

total = 0

even = 0

odd = 0

while n > 0:
    digit = n % 10
    count += 1
    total += digit

    if digit % 2 == 0:
        even += 1
    else:
        odd += 1

    n //= 10

print("Number of digits:", count)

print("Sum of digits:", total)

print("Even digits:", even)

print("Odd digits:", odd)

if total % 2 == 0:
    print("The sum is even")
else:
    print("The sum is odd")


#15 sxvadasxva ricxvi



numbers = []

for i in range(15):
    n = int(input("Enter a number: "))
    numbers.append(n)

positive = 0
negative = 0
zero = 0

for n in numbers:
    if n > 0:
        positive += 1
    elif n < 0:
        negative += 1
    else:
        zero += 1

largest = max(numbers)
smallest = min(numbers)
average = sum(numbers) / 15

print("Largest number:", largest)

print("Smallest number:", smallest)

print("Positive numbers:", positive)

print("Negative numbers:", negative)

print("Zeros:", zero)

print("Average:", average)

if average > 0:
    print("Average is positive")
elif average < 0:
    print("Average is negative")
else:
    print("Average is zero")


# ricxvis gamocnoba


secret = 37

attempts = 7

for i in range(attempts):
    guess = int(input("Guess the secret number: "))

    if guess == secret:
        print("Congratulations! You guessed correctly!")
        break
    elif guess < secret:
        print("The secret number is bigger")
    else:
        print("The secret number is smaller")

else:
    print("Game over! The correct number was:", secret)



#fizzbuzz


start = int(input("Enter the starting number: "))

end = int(input("Enter the ending number: "))

fizz = 0

buzz = 0

fizzbuzz = 0

for i in range(start, end + 1):

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        fizzbuzz += 1

    elif i % 3 == 0:
        print("Fizz")
        fizz += 1

    elif i % 5 == 0:
        print("Buzz")
        buzz += 1

    else:
        print(i)

print("Fizz count:", fizz)

print("Buzz count:", buzz)

print("FizzBuzz count:", fizzbuzz)










