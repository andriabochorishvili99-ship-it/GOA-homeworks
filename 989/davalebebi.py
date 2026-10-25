# 5) მომხმარებელს შემოაყვანინეთ თავისი ასაკი, შემდგომ იმ შემთხვევაში თუ მისი ასაკი მეტია 18-ზე დაეწერეთ "You are adult!", ყველა სხვა შემთხვევაში დაუწერეთ "You are not adult!".

# 6) მომხმარებელს შემოაყვანინეთ ერთი რიცხვი, შემდგომ შეამომწეთ, იმ შემთხვევაში თუ რიცხვი ლუწია გამოუტანეთ ტერმინალში "Your number is even!" ყველა სხვა შემთხვევაში "Your number is odd!"

# 7) მომხმარებელს შემოაყვანინეთ სამი რიცხვი, თქვენი დავალებაა გაარკვიოთ ამ სამიდან რომელი რიცხვი არის ყველაზე დიდი, გამოიყენეთ if, elif და else.
    
#5
age = int(input('please enter age: '))

if age >= 18:
    print('you are adult')

else:
    print('you are not adult')


#6


num = int(input('please enter number: '))



if num is even:
    print('your number is even')

else:
    print('your number is odd')


