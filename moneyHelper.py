# MONEY HELPER FOR YOU #

# IMPORT ALL NEED LIBRARIES #
from collections import namedtuple
import csv
from csv import writer

# DICTIONARY WHERE WE WILL STORE INFORMATION #
OperationAdd = namedtuple("AccountInfo", ['Name', 'Balance'])

# SOME VARIABLES #

# USER ID #
account_id = 1
# HERE WE STORE ACCOUNT INFO FOR UPDATE #
acc_info = []
# VARIABLE FOR CHECK USER LOGIN  #
log_info = False
# VARIABLE FOR CHECK USER REGISTRATION #
created_account = False

create_balance = 0

# MAIN CLASS #
class MoneyHelper:
    # CONSTRUCTOR #
    def __init__(self):
        self.name = ''
        self.__balance = 0

    # REGISTRATION METHOD #
    def registration(self, name='Unknown', balance=0.0):
        global account_id
        # HERE WE TAKE VALUE SROM USER #
        self.name = name
        self.__balance = balance
        create_balance = self.__balance
        # HERE WE STORE 'acc_info' INFORMATION #
        acc_info.append(account_id)
        acc_info.append(self.name)
        acc_info.append(self.__balance)
        # HERE WE STORE INFORMATION IN '.csv' FILE #
        with open('project.csv', 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(acc_info)
            f_object.close()
        print('Register successful.')

    # ADD MONEY ON BALANCE METHOD #
    def addOperation(self, howMany=0.0):
        # COUNT USER BALANCE AFTER ADDING MONEY #
        self.__balance = self.__balance + howMany
        bal = float(self.__balance)
        global account_id
        # HERE WE STORE NEW INFORMATION ABOUT USER ACCONT #
        acc_info.insert(0, account_id)
        acc_info.insert(1, self.name)
        acc_info.insert(2, bal)
        # HERE WE WRITE NEW INFORMATION ABOUT USER #
        with open('project.csv', 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(acc_info)
            f_object.close()
        print('Operation add')

    # MINUS MONEY FROM BALANCE #
    def minusMoney(self, howMany=0.0):
        # HERE WE CHECK THAT USER HAVE ENOUGHT MONEY #
        if howMany > self.__balance:
            print('You dont have enought money')
        # IF HAVE ENOUGHT MONEY #
        elif howMany < self.__balance:
            # COUNT NEW USER BALANCE #
            self.__balance = self.__balance - howMany
            bal = float(self.__balance)
            global account_id
            # STORE NEW INFORMATION ABOUT USER #
            acc_info.insert(0, account_id)
            acc_info.insert(1, self.name)
            acc_info.insert(2, bal)
            # HERE WE WRITE NEW INFORMATION ABOUT USER #
            with open('project.csv', 'a', newline='') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow(acc_info)
                f_object.close()
            print('Your money divided')
        else:
            print('Try again')

    # CHECK BALANCE AND ACCOUNT INFO #
    def checkAccInfo(self, project):
        result = {}
        # HERE WE SHOW ALL INFORMATION ABOUT USER #
        for row in csv.reader(open(project)):
            number = int(row[0])
            name = row[1]
            balance = row[2]
            result[number] = OperationAdd(name, balance)
        return result

    # LOGIN METHOD #
    def login(self, name, project):
        main_bal = 0
        # CHECK TWO VARIABLES #
        global log_info
        global created_account
        result = {}
        # STORE USER INPUT FOR CHECK #
        self.name = name
        # CHECKING IF USER INPUT EXIST IN '.csv' FILE #
        for row in csv.reader(open(project)):
            number = int(row[0])
            login = row[1]
            balance = float(row[2])
            main_bal = balance
            # IF NAME EXIST #
            if self.name == login:
                # HERE WE CHANGE VARIABLE TO TRUE #
                created_account = True
                log_info = True
                self.name = login
                self.__balance = balance


    # DESTRUCTOR #
    def __del__(self):
        return self.name, self.__balance


# STORE CLASS IN VARIABLE FOR FUTURE USE #
user = MoneyHelper()


# FUNCTION WITH START MENU #
def startMenu(project):
    global created_account
    global log_info
    # HERE START MENU #
    choose = input('Menu:\n'
                   '1 - Create account\n'
                   '2 - Login\n'
                   '3 - Exit\n'
                   'Choose: ')
    # HERE WE CHECKING USER CHOICE FOR KNOW WHAT TO DO #
    if choose == '1':
        checkNumber = ''
        for row in csv.reader(open(project)):
            checkNumber = row[0]
        if checkNumber == '1':
            print('You have account. Just login.')
            startMenu('project.csv')
        else:
            # HERE USER ENTER NAME #
            name = input('Enter name: ')
            # HERE USER ENTRE BALANCE #
            balance = float(input('Enter balance: '))
            # HERE CALL METHOD TO REGISTER NEW USER #
            user.registration(name, balance)
            # CHANGE VARIABLE TO TRUE #
            created_account = True
            # CALL MAIN MENU #
            engine()
    elif choose == '2':
        # USER INPUT NAME FOR CHECK IF ITS EXIST #
        name = input('Enter name: ')
        # CALL METHOD FROM CLASS TO CHECK #
        user.login(name, 'project.csv')
        # IF EXIST CALL FUNCTION WITH MAIN MENU #
        if log_info:
            print('Login successful.')
            engine()
        else:
            print('Try again or register.')
            startMenu('project.csv')
    elif choose == '3':
        exit()
    else:
        print('Try again.')
        startMenu('project.csv')


# FUNCTION WITH MAIN MENU AND ENGINE #
def engine():
    global created_account
    # HERE MEIN MENU #
    choose = input('Menu:\n'
                   '1 - Add operation\n'
                   '2 - Minus operation\n'
                   '3 - Check account balance\n'
                   '4 - Exit\n'
                   'Choose: ')
    # HERE WE CHECK USER CHOICE FOR KNOW WHAT TO DO #
    if choose == '1':
        # CHECK IF ACCOUNT CREATED USER CAN ADD MONEY #
        if created_account:
            # HERE ENTER HOW MANY MONEY #
            howMany = float(input('How many money u wanna put: '))
            # HERE CALL METHOD FROM CLASS TO ADD MONEY #
            user.addOperation(howMany)
            # CALL MAIN MENU #
            engine()
        else:
            print('For do this operation create account!')
            engine()
    elif choose == '2':
        # CHECK IF ACCOUNT CREATED USER CAN DIVIDE MONEY #
        if created_account:
            # HERE ENTER HOW MANY MONEY #
            howMany = float(input('How many money u wanna get: '))
            # HERE CALL METHOD FROM CLASS TO DIVIDE MONEY #
            user.minusMoney(howMany)
            # CALL MAIN MENU #
            engine()
    elif choose == '3':
        # CHECK IF ACCOUNT CREATED USER CAN CHECK HIS INFO #
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


# CALL MAIN FUNCTION TO START PROGRAM  #
startMenu('project.csv')
