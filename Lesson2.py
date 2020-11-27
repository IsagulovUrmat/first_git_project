# def add(numb1,numb2,numb3):
  #  print(numb1+numb2+numb3)

#def greetings(name:str,lastname):
 #   return f'Hello, {name} {lastname}. Ur welcome!'

#name = input('Input your name:')
#lastname = input('Input your last name:')
#print(greetings(name,lastname))

def calc(number1:int,number2:int,sign:str):
    if sign == '+':
        print(number1 + number2)
    elif sign == '-':
        print(number1 - number2)
    elif sign == '*':
        print(number1 * number2)
    elif sign == '/':
        print(number1 // number2)
    else:
        print('Вы ввели не тот символ!')

        sig = input('Какую операцию вы хотите выполнить?')
        num1 = int(input('Введите первое число:'))
        num2 = int(input('Введите первое число:'))

        #calc(num1,num2,sig)

x = int(input())
print(x // 100)
print(x //10 % 10)
print(x % 100 % 10)







