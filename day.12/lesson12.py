
# BONUS
# ციკლისა და პირობითი ოპერატორების გამოყენებით იპოვეთ სიაში ყველაზე დიდი რიცხვი max() ფუნქციის გამოყენების გარეშე.

# 5) შექმენით პროგრამა, რომელშიც წინასწარ გექნებათ მოცემული 3 ფილმისგან შემდგარი სია.

# პროგრამამ უნდა:

# - დაბეჭდოს ყველა ფილმი for ციკლის გამოყენებით;
# - მომხმარებელს შეაყვანინოს ახალი ფილმის სახელი და დაამატოს ის სიაში (მოიძიეთ ინფორმაცია .append() მეთოდის შესახებ);
# - მომხმარებელს შეაყვანინოს ინდექსი და დაბეჭდოს ამ ინდექსზე არსებული ფილმი


#ricxvebi

# num = [1, 2, 3, 4, 5]

# print(num[0])

# print(num[-1])

# print(num[3])



# for i in num:
#     print(i)


# enter = int(input('please enter number: '))

# if enter in num:
#     print('the number is in the list')
# else:
#     print('the number is not in the list')



#qulebi



# score = [ 50, 70, 90, 30, 40, 60]



# for i in score:
#     print(i)

# print(len([i for i in score if i >= 50]))


# print(len([i for i in score if i < 50]))



#dadebitia tu uaryofiti


# numbers = [ 9 , 14 ,-25 , 0 ,37 , 55 , 99]

# print(numbers)


# print('positive numbers:', len([i for i in numbers if i > 0]))

# print('negative numbers: ', len([i for i in numbers  if  i < 0]))

# print('equal to zero: ', len([i for i in numbers if i == 0]))


#filmi


aa = ['spider-man', 'The Godfather', 'iron man']

bb = input('please enter movie name: ')

aa.append(bb)

print(aa)




