#dadebitia uaryofiti tu nulis tolia

num = int(input('please enter number: '))

if num > 0:
    print('positive')
elif num < 0:
    print('negative')

else:
    print('equal to 0')



# 90–100 ქულა — A
# 80–89 ქულა — B
#  70–79 ქულა — C
#  60–69 ქულა — D
#  0–59 ქულა — F

score = int(input('please enter your point: '))


if score  < 0 or score> 100:
    print('score is incorect')
elif score >= 90:
    print('A')
elif score >= 70:
    print('B')

elif score >= 60:
    print('C')

else:
    print('F')

#ricxvis gamocnoba

secret = 89

guess = int(input('please enter number: '))

while guess != secret:
    print('incorect')
    guess = int(input('try again: '))

print('coungratulations, you gussed number')

# + - * //

num1 = float(input('please enter number: '))

num2 = float(input('please enter number: '))

op = input('enter operation(+ , - , * , // ): ')

if op == '+':
    print(num1 + num2)
    print('wrong')
    int(input('try again: '))

elif op == '-':
    print(num1- num2)
    print('wrong')
    int(input('try again: '))

elif op == '*':
    print(num1 * num2)
    print('wrong')
    int(input('try again: '))

elif op == '//':
    print(num1 // num2)
    print('wrong')
    int(input('try again: '))

else:
    print('wrong operation')







