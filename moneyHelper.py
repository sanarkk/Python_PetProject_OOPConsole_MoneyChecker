# MONEY HELPER FOR YOU #

class MoneyHelper:

    def __init__(self):
        self.name = ''
        self.__balance = 0
        self.description = ''

    def registration(self, name='Unknown', balance=0.0):
        self.name = name
        self.__balance = balance

        print('Register successful')

    def addOperation(self, howMany=0.0, description=''):
        self.__balance = self.__balance + howMany
        self.description = description

        print('Operation add')

    def minusMoney(self, howMany=0.0, description=''):
        self.__balance = self.__balance - howMany
        self.description = description

        print('Your money divided')

    def info(self):
        return self.name, self.__balance, self.description

    def __del__(self):
        return self.name, self.__balance, self.description


user = MoneyHelper()
created_account = False


def engine():
    global created_account
    choose = input('Menu:\n'
                   '1 - Create account\n'
                   '2 - Add operation\n'
                   '3 - Minus operation\n'
                   '4 - Check my info\n'
                   '5 - Exit\n'
                   'Choose: ')
    if choose == '1':
        name = input('Enter name: ')
        balance = float(input('Enter balance: '))
        user.registration(name, balance)
        created_account = True
        engine()
    elif choose == '2':
        if created_account:
            howMany = float(input('How many money u wanna put: '))
            description = input('Enter where u taked this money: ')
            user.addOperation(howMany, description)
            engine()
        else:
            print('For do this operation create account!')
            engine()
    elif choose == '3':
        if created_account:
            howMany = float(input('How many money u wanna get: '))
            description = input('Enter for what u taked this money: ')
            user.minusMoney(howMany, description)
            engine()
        else:
            print('For do this operation create account!')
            engine()
    elif choose == '4':
        if created_account:
            print(user.info())
            engine()
        else:
            print('For do this operation create account!')
            engine()
    elif choose == '5':
        exit()
    elif choose == '':
        print('Enter again!')
        engine()
    else:
        print('Enter again!')
        engine()


engine()
