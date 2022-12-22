from entities import *
from errors import *

list_names = []
currencies = ["BGN", "EUR", "USD", "JPY"]
acc_types = ["Current", "Savings", "Credit"]
list_users = []
list_accounts = []
list_accounts_names = []
class Menu:
    def print_menu(self):
        print("1. Create a new user")
        print("2. Create account for existing user")
        print("3. Print all existing users")
        print("4.. Print all existing accounts")
        print("5. Deposit for user account")
        print("6. Withdraw")
        print("7. Exit")


    def command_create_user(self, names, EGN):
        return names, EGN


    def command_create_account(self, balance, currency, acc_type, IBAN):
        return balance, currency, acc_type, IBAN


    def command_print_users(self):
        pass

    def command_print_accounts(self):
        pass

    def command_deposit(self):
        pass

    def command_withdraw(self):
        pass

    def run(self):
        # infinite menu loop
        while True:
            Menu.print_menu(self)
            # ...

            # ask the user to choose a command
            choice = input("Choose an item from the menu: \n> ")

            # catch errors
            try:

                # process the user's choice
                if choice == "1":
                    # ask the user to input the necessary command parameters
                    name = input("Enter name(must be more than 4 letters): ")
                    if len(name) < 4:
                        raise InvalidName("Invalid name")
                    if name in list_names:
                        raise CharacterExists("Name already exists")
                    if name.isdigit():
                        raise InvalidName("Not supporting numbers")
                    EGN = input("Enter EGN(10 numbers): ")

                    if EGN.isalpha():
                        raise InvalidEGN("Invalid EGN")

                    if len(EGN) < 10:
                        raise InvalidEGN
                    all_users = self.command_create_user(name, EGN)
                    print(all_users)
                    list_users.append(all_users)
                    list_names.append(name)
                    continue
                if choice == "2":
                    name = input("Enter username: ")
                    if name in list_names:
                        account = input("Enter account: ")
                        balance = float(input("Enter balance(digits-only): "))
                        if type(balance) != float:
                            raise InvalidDataFormat
                        currency = input("Enter currency(BGN, EUR, USD, JPY): ")
                        if not currency in currencies:
                            raise InvalidAccCurrency

                        acc_type = input("Enter account type(Current, Savings, Credit): ")
                        if not acc_type in acc_types:
                            raise InvalidAccountType
                        acc = self.command_create_account(account, balance, currency, acc_type)
                        list_accounts.append(acc)
                        list_accounts_names.append(account)
                        print(acc)
                        continue
                    else:
                        raise InvalidName
                if choice == "3":
                    print(f"{list_users}")
                    continue
                if choice == "4":
                    print(f"{list_accounts}")
                    continue
                if choice == "5":
                    account = input("Enter account: ")
                    if account in list_accounts_names:
                        deposit_money = float(input("Enter money(number): "))
                        if type(deposit_money) != float:
                            raise InvalidDataFormat
                        else:
                            print(f"{deposit_money} deposited")
                            continue
                    else:
                        raise AccountNotFound("This account doesn't exist")
                if choice == "6":
                    account = input("Enter account: ")
                    if account in list_accounts_names:
                        withdraw = float(input("Enter money(number): "))
                        #if withdraw > balance:
                        #    pass
                        if type(withdraw) != float:
                            raise InvalidDataFormat
                        else:
                            print(f"{withdraw} withdrawed")
                            continue
                    else:
                        raise AccountNotFound("This account doesn't exist")
                if choice == "7":
                    break
                else:
                    raise InvalidCommand("Invalid choice")




            except Exception as ex:
                print(f"Error: {str(ex)}")

            print()


if __name__ == '__main__':

    menu = Menu()
    menu.run()
    print()

