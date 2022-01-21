# MONEY HELPER FOR YOU #

# IMPORT ALL NEED LIBRARIES #
from collections import namedtuple
import csv
from csv import writer

# DICTIONARY WHERE WE WILL STORE INFORMATION #
OperationAdd = namedtuple("AccountInfo", ['Name', 'Balance'])
acc_info = []

PROJECT_URL = 'project.csv'

account_id = 1
login_account = False
created_account = False

"""MAIN CLASS"""
class MoneyHelper:

    def __init__(self):
        self.name = ''
        self.__balance = 0

    def registration(self, name='Unknown', balance=0.0):
        global created_account
        self.name = name
        self.__balance = balance
        acc_info.append(account_id)
        acc_info.append(self.name)
        acc_info.append(self.__balance)
        with open('project.csv', 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(acc_info)
            f_object.close()
        created_account = True
        print('Register successful.')

    def operation(self, how, howMany=0.0):
        global account_id
        balance = 0.0
        operationText = ''
        if how == 1:
            balance = self.__balance + howMany
            operationText = '\'add money\''
        elif how == 2:
            if howMany > self.__balance:
                print('You don\'t have enough money')
            else:
                balance = self.__balance - howMany
                operationText = '\'withdraw money\''
        acc_info.insert(0, account_id)
        acc_info.insert(1, self.name)
        acc_info.insert(2, balance)
        with open('project.csv', 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(acc_info)
            f_object.close()
        print(f'Operation: {operationText}, successful.')

    # CHECK BALANCE AND ACCOUNT INFO #
    @staticmethod
    def checkAccInfo(project):
        result = {}
        for row in csv.reader(open(project)):
            number = int(row[0])
            name = row[1]
            balance = row[2]
            result[number] = OperationAdd(name, balance)
        return result

    def login(self, name, project):
        global login_account
        self.name = name
        for row in csv.reader(open(project)):
            number = int(row[0])
            login = row[1]
            balance = float(row[2])
            if self.name == login:
                self.name = login
                self.__balance = balance
                login_account = True

    def __del__(self):
        return self.name, self.__balance


user = MoneyHelper()


def startMenu(project):
    user_choice = input('Menu:\n'
                        '1 - Create account\n'
                        '2 - Login\n'
                        '3 - Exit\n'
                        'Choose: ')
    if user_choice == '1':
        check_exist_id = ''
        for row in csv.reader(open(project)):
            check_exist_id = row[0]
        if check_exist_id == '1':
            print('You have account. Just login.')
            startMenu(PROJECT_URL)
        else:
            user_name = input('Enter name: ')
            user_balance = float(input('Enter balance: '))
            user.registration(user_name, user_balance)
            operationMenu()
    elif user_choice == '2':
        user_name = input('Enter name: ')
        user.login(user_name, PROJECT_URL)
        if login_account:
            print('Login successful.')
            operationMenu()
        else:
            print('Try again or register.')
            startMenu(PROJECT_URL)
    elif user_choice == '3':
        exit()
    else:
        print('Try again.')
        startMenu(PROJECT_URL)


# FUNCTION WITH MAIN MENU AND ENGINE #
def operationMenu():
    user_choice = input('Menu:\n'
                        '1 - Operation: \'add money\'\n'
                        '2 - Operation: \'withdraw money\'\n'
                        '3 - Check account balance\n'
                        '4 - Exit\n'
                        'Choose: ')
    if user_choice == '1':
        user_amount = float(input('Enter amount: '))
        user.operation(1, user_amount)
        operationMenu()
    elif user_choice == '2':
        user_amount = float(input('Enter amount: '))
        user.operation(2, user_amount)
        operationMenu()
    elif user_choice == '3':
        account_info = user.checkAccInfo(PROJECT_URL)
        print(account_info)
        operationMenu()
    elif user_choice == '4':
        exit()
    elif user_choice == '':
        print('Enter again!')
        operationMenu()
    else:
        print('Enter again!')
        operationMenu()


if __name__ == "__main__":
    startMenu(PROJECT_URL)
