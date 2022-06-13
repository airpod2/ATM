import random
'''
Requirements
At least the following flow should be implemented:

Insert Card => PIN number => Select Account => See Balance/Deposit/Withdraw

For simplification, there are only 1 dollar bills in this world, no cents. 
Thus account balance can be represented in integer.
'''

class ATM():
    def __init__(self):
        self.balance = 0
        self.account = None
        self.chance = 5
        self.cardNum = None

    
    def read_card(self, cardNum):
        '''card reader would tell the card number'''
        print("*** Insert a card ***")
        if len(str(cardNum)) == 16 and str(cardNum).isdecimal():
            self.cardNum = cardNum
            return self.cardNum
        else:
            print("*** Invalid card. Please try again ***")
            self.exit_menu()

    def PIN(self):
        '''prompt user to enter the PIN'''
        print("Enter your PIN (4 digit)")
        pinNum = int(input(">>> ")[:4])
        if pinNum > 0:
            return pinNum

    def verify_PIN(self, isCorrect):
        '''bank API would tell me if PIN number is correct or not'''
        if isCorrect:
            return True
        else:
            self.chance -= 1   
            print("*** Wrong PIN. Please try agian *** \n(attempts remaning : %d)\n" % self.chance)
    
            if self.chance == 0:
                print("Please take your card")
                self.exit_menu()

    def select_account(self, accounts):
        '''bank API would tell me what kinds of the account user have'''
        account_type = { 
            1 : "Checking account",
            2 : "Savings account",
            3 : "Credit Card",
            4 : "Other"
        }
        print('\n*** Please select an account ***')
        for i in accounts:
            print(str(i) + " " + account_type[i])

        option = int(input("Enter the option >>> "))
        
        if option not in accounts:
            print("*** The option doesn't exist ***\n" )
            return "error"

        self.account = option
        return self.account
    
    def load_account(self, balance):
        '''get information(ex balance) of the account from bank system'''
        self.balance = balance

    def show_menu(self):
        '''ATM menu'''
        # Improvements : show proper menu for each account type
        # Improvements : print a recipt
        print("\n*** Please select a transaction ***")
        print("[1] Balance Inquiry")
        print("[2] Deposit")
        print("[3] Withdrawal")
        print("[4] Exit")
        
        option = int(input('Enter the option >>> '))
        if option in [1,2,3,4]:
            {
                1 : self.check_balance,
                2 : self.deposit,
                3 : self.withdraw,
                4 : self.exit_menu
            }[option]()
        else:
            print("*** The option doesn't exist ***" )
            self.another_transaction()
        
    def check_balance(self):
        print("Balance Inquiry")
        print(self.balance)
        return self.balance

    def deposit(self):
        print("Enter the amount you wish to deposit")
        deposit = int(input(">>> "))
        if deposit > 0:
            self.balance += deposit
            print("Your transaction has been successful")
            print(self.balance)
            return self.balance
        else:
            print("*** Wrong amount ***")
            # self.deposit()
            self.another_transaction()
            
    def withdraw(self): 
        print("Enter the amount you wish to withdraw")
        withdrawal = int(input(">>> "))
        if withdrawal < self.balance and withdrawal > 0:
            self.balance -= withdrawal
            print("Your transaction has been successful")
            print(self.balance)
            return self.balance
        else:
            print("Your balance : ", self.balance)
            # self.withdraw()
            self.another_transaction()

    def exit_menu(self):
        print("\nThank you for banking with us")
        exit()

    def another_transaction(self): 
        print("\nWould you like to make another transaction?")
        yes = input("y / n >>> ")
        if yes == 'y':
            self.show_menu() 
        else:
            self.exit_menu()

def main():
    verified = False
    atm = ATM()

    while atm.cardNum is None:
        cardNum = 1234567890123456 #card reader -> ATM
        atm.read_card(cardNum) 
    
    while not verified:
        pin = atm.PIN()
        
        '''cardNum, PIN --Bank-> if correct --ATM-> isCorrect, userID, balance, accounts'''
        isCorrect = random.choice([True, False]) #Bank -> ATM
        verified = atm.verify_PIN(isCorrect)
    
    if verified:
        atm.load_account(10000) #Bank -> ATM
        accounts = [1,2,4] #Bank -> ATM
        
        while atm.account == 0 :
            account = atm.select_account(accounts)
        
        atm.show_menu()
        while True:
            atm.another_transaction()
            
    '''userID, account, updated info(ex) balance) --ATM-> Bank'''

if __name__ == "__main__":
    main()