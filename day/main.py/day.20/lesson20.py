fruits = {'apple', 'banana', 'orange', 'grape', 'mango', 'pear'}

new_fruit = input('Enter a new fruit name: ')

fruits.add(new_fruit)

print(fruits)


students = {'Giorgi', 'Nino', 'Luka', 'Mariam', 'Dato'}

student_name = input('Enter a student name: ')

if student_name in students:
    print(f'{student_name} is in the set.')
else:
    print(f'{student_name} is not in the set.')



numbers = {10, 20, 30, 40, 50, 60, 70}

num = int(input('Enter a number: '))

if num in numbers:
    numbers.remove(num)
    print('Updated set:', numbers)
else:
    print('Number not found in the set.')















