# MONEY HELPER FOR YOU #
from collections import namedtuple
import csv
from csv import writer

OperationAdd = namedtuple("AccountInfo", ['Name', 'Balance'])
account_id = 1
acc_info = []
log_info = False


class MoneyHelper:

    def __init__(self):
        self.name = ''
        self.__balance = 0

    def registration(self, name='Unknown', balance=0.0):
        global account_id
        self.name = name
        self.__balance = balance
        acc_info.append(account_id)
        acc_info.append(self.name)
        acc_info.append(self.__balance)
        with open('project.csv', 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(acc_info)
            f_object.close()
        print('Register successful')

    def addOperation(self, howMany=0.0):
        self.__balance = self.__balance + howMany
        global account_id
        acc_info.append(account_id)
        acc_info.append(self.name)
        acc_info.append(self.__balance)
        with open('project.csv', 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(acc_info)
            f_object.close()
        print('Operation add')

    def minusMoney(self, howMany=0.0):
        if howMany > self.__balance:
            print('You dont have enought money')
        elif howMany < self.__balance:
            self.__balance = self.__balance - howMany
            global account_id
            acc_info.append(account_id)
            acc_info.append(self.name)
            acc_info.append(self.__balance)
            with open('project.csv', 'a', newline='') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow(acc_info)
                f_object.close()
            print('Your money divided')
        else:
            print('Try again')

    def checkAccInfo(self, project):
        result = {}
        for row in csv.reader(open(project)):
            number = int(row[0])
            name = row[1]
            balance = row[2]
            result[number] = OperationAdd(name, balance)

        return result

    def login(self, name, project):
        global log_info
        global created_account
        result = {}
        self.name = name
        for row in csv.reader(open(project)):
            number = int(row[0])
            login = row[1]
            balance = float(row[2])
            if self.name == login:
                created_account = True
                print('login successful')
                log_info = True
                self.__balance = balance

            else:
                print('Try again')

    def __del__(self):
        return self.name, self.__balance


user = MoneyHelper()
created_account = False


def startMenu():
    global created_account
    global log_info
    choose = input('Menu:\n'
                   '1 - Create account\n'
                   '2 - Login\n'
                   '3 - Exit\n'
                   'Choose: ')
    if choose == '1':
        name = input('Enter name: ')
        balance = float(input('Enter balance: '))
        user.registration(name, balance)
        created_account = True
        engine()
    elif choose == '2':
        name = input('Enter name: ')
        user.login(name, 'project.csv')
        if log_info:
            engine()
        else:
            startMenu()
    elif choose == '3':
        exit()
    else:
        print('Try again.')
        startMenu()


def engine():
    global created_account
    choose = input('Menu:\n'
                   '1 - Add operation\n'
                   '2 - Minus operation\n'
                   '3 - Check account balance\n'
                   '4 - Exit\n'
                   'Choose: ')

    if choose == '1':
        if created_account:
            howMany = float(input('How many money u wanna put: '))
            user.addOperation(howMany)
            engine()
        else:
            print('For do this operation create account!')
            engine()
    elif choose == '2':
        if created_account:
            howMany = float(input('How many money u wanna get: '))
            user.minusMoney(howMany)
            engine()
    elif choose == '3':
        if created_account:
            resultMM = user.checkAccInfo('project.csv')
            print(resultMM)
            engine()
        else:
            print('For do this operation create account!')
            engine()
    elif choose == '4':
        exit()
    elif choose == '':
        print('Enter again!')
        engine()
    else:
        print('Enter again!')
        engine()


startMenu()
