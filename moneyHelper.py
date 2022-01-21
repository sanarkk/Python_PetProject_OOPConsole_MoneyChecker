from collections import namedtuple
import csv
from csv import writer

# DICTIONARY WHERE WE WILL STORE INFORMATION #
Operation = namedtuple("AccountInfo", ['Name', 'Balance'])
acc_info = []

PROJECT_URL = 'project.csv'

"""USER BALANCE"""
class Balance:

    def __init__(self):
        self.balance = 0.0

    def __del__(self):
        return self.balance
bal = Balance()


"""CHECK ACCOUNT STATUS"""
class AccStatus:
    def __init__(self):
        self.login_account = False
        self.created_account = False

    def __del__(self):
        return self.login_account, self.created_account
acc = AccStatus()


"""USER CLASS"""
class MoneyHelper(Balance, AccStatus):

    def __init__(self):
        super().__init__()
        self.name = ''
        self.id = 1

    def registration(self, name='Unknown', balance=0.0):
        self.name = name
        bal.balance = balance
        acc_info.append(self.id)
        acc_info.append(self.name)
        acc_info.append(bal.balance)
        with open('project.csv', 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(acc_info)
            f_object.close()
        acc.created_account = True
        print('Register successful.')

    @staticmethod
    def checkAccInfo(project):
        result = {}
        for row in csv.reader(open(project)):
            number = int(row[0])
            name = row[1]
            bal.balance = row[2]
            result[number] = Operation(name, bal.balance)
        return result

    def login(self, name, project):
        username = name
        login = ''
        for row in csv.reader(open(project)):
            number = int(row[0])
            login = row[1]
            balance = float(row[2])
        if username == login:
            self.name = login
            bal.balance = balance
            acc.login_account = True
        else:
            self.name = ''
            acc.login_account = False
            print('.......')

    def __del__(self):
        return self.name, self.id
user = MoneyHelper()

"""CLASS WHICH CHECK USER OPERATIONS"""
class OperationChecker(MoneyHelper):

    def __init__(self):
        self.operation = 0
        self.operationText = ''

    def Operation(self, operation, howMany=0.0):
        if operation == 1:
            bal.balance = float(bal.balance) + float(howMany)
            self.operationText = '\'add money\''
        elif operation == 2:
            if float(howMany) > float(bal.balance):
                print('You don\'t have enough money')
                self.operationText = 'not'
            else:
                bal.balance = float(bal.balance) - float(howMany)
                self.operationText = '\'withdraw money\''

        acc_info.insert(0, user.id)
        acc_info.insert(1, user.name)
        acc_info.insert(2, bal.balance)
        with open('project.csv', 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(acc_info)
            f_object.close()
        print(f'Operation: {self.operationText} successful.')

    def __del__(self):
        return self.operation, self.operationText
check = OperationChecker()

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
        if acc.login_account:
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
        check.Operation(1, float(user_amount))
        operationMenu()
    elif user_choice == '2':
        user_amount = float(input('Enter amount: '))
        check.Operation(2, float(user_amount))
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
