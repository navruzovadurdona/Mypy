import random

number = random.randint(1, 100)
guess = None

while guess != number:
    guess = int(input("Угадайте число от 1 до 100: "))
    if guess < number:
        print("Слишком маленькое число. Попробуйте снова.")
    elif guess > number:
        print("Слишком большое число. Попробуйте снова.")
    else:
        print("Поздравляю! Вы угадали число.")
        break
