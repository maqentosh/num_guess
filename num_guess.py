# from random import randint

# def play():
#     global counter
#     global guessed_num

#     try:
#         num = int(input('ваше число: '))
#         counter += 1

#         if num == guessed_num:
#             print('Вы лошок, но угадали!')
#             print(f'Количество попыток :{counter}')
#         elif num > guessed_num:
#             print('загадонное число меньше')

#             play()
#         elif num < guessed_num:
#             print('загадонное число больше')

#             play()
#         else:
#             play()

#     except ValueError:
#         play()
    

# def init():
#     global guessed_num
#     global user
#     global counter

#     guessed_num = randint(1, 25)
#     print(f'Отлино {user}, загаданное число находится между 1 и 25. Удачи')
#     counter = 0


# def start():
#     confirmation = input('Хотите сыграть? (да/нет)\n')

#     if confirmation.lower().startswith('д'):
#         global user

#         user = input('Пожалуйста введите ваше имя: ').capitalize()

#         init()
#         play()
#     elif confirmation.lower().startswith(('n', 'н')):
#         print('а нафиг ты сюда зашел, идиот -_-')
#     else:
#         print('Такого варианта нет. Попробуйте еще раз, но врядли это поможет')

# start()


# while True:
#     try:
#         num1 = int(input('enter the 1st number: '))
#         num2 = int(input('enter the 2nd number: '))
#         char = input('enter the operation: ')
#         if char == '+':
#             print(num1+num2)
#         elif char == '-':
#             print(num1-num2)
#     except:
#         print('incorrect value')
#         break



# while True:
#     try:
#         print(eval(input('введите и выйдите')))
#     except ZeroDivisionError:
#         print('на 0 делить нельзя, неуч!')
#     except KeyboardInterrupt:
#         print('you stopped the program')
#         break
#     except: 
#         print('неверно Пробуй ввести числа')