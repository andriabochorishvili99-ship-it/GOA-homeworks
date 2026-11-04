#ricxvebi

num = [1, 2, 3, 4, 5]

print(num[0])

print(num[-1])

print(num[3])



for i in num:
    print(i)


enter = int(input('please enter number: '))

if enter in num:
    print('the number is in the list')
else:
    print('the number is not in the list')



#qulebi



score = [ 50, 70, 90, 30, 40, 60]



for i in score:
    print(i)

print(len([i for i in score if i >= 50]))


print(len([i for i in score if i < 50]))



#dadebitia tu uaryofiti


numbers = [ 9 , 14 ,-25 , 0 ,37 , 55 , 99]

print(numbers)


print('positive numbers:', len([i for i in numbers if i > 0]))

print('negative numbers: ', len([i for i in numbers  if  i < 0]))

print('equal to zero: ', len([i for i in numbers if i == 0]))


#filmi


movies = ['spiderman', 'ironman', 'the godfather']


print('movies on list')
for movie in movies:
    print(f"- {movie}")

print()  

new_movie = input('please enter new name: ')
movies.append(new_movie)

print(f"ახალი სია: {movies}\n")


index = int(input(f'enter index(0-დან {len(movies) - 1}-მდე): '))


if 0 <= index < len(movies):
    print(f'chose index ({index}) chose film: {movies[index]}')
else:
    print('isnt in list')


