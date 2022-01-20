# MONEY HELPER FOR YOU #
from collections import namedtuple
import csv
from csv import writer


OperationAdd = namedtuple("AccountInfo", ['Name', 'Balance'])
account_id = 1
acc_info = []


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

    def addOperation(self, howMany=0.0, description=''):
        self.__balance = self.__balance + howMany
        global account_id
        acc_info.insert(2, self.__balance)
        with open('project.csv', 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(acc_info)
            f_object.close()
        print('Operation add')

    def minusMoney(self, howMany=0.0, description=''):
        if howMany > self.__balance:
            print('You dont have enought money')
        elif howMany < self.__balance:
            self.__balance = self.__balance - howMany
            global account_id
            acc_info.insert(2, self.__balance)
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

    def __del__(self):
        return self.name, self.__balance


user = MoneyHelper()
created_account = False


def engine():
    global created_account
    choose = input('Menu:\n'
                   '1 - Create account\n'
                   '2 - Add operation\n'
                   '3 - Minus operation\n'
                   '4 - Check account balance\n'
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
            resultMM = user.checkAccInfo('project.csv')
            print(resultMM)
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
