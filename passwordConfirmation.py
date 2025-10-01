correctPassword3 = "Admin123"

def enterYourPassword():
    while True:
        enterPassword = input('Введите пароль: ')
        if enterPassword == correctPassword3:
            print("Вы успешно авторизовались!")
            break
        else:
            print("Попробуйте еще раз: ")


