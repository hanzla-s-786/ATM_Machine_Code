import time

def atm_simulator():
    password = 2332
    balance = 5000
    account_number_1 = 12345
    account_number_2 = 54321
    wrong_pin_count = 0

    while True:
        print("Please insert your card")
        time.sleep(4)

        pin = int(input("Enter your ATM PIN : "))

        if pin == password:
            wrong_pin_count = 0  # Reset wrong pin count
            print("""
                1 == Balance
                2 == Withdraw balance
                3 == Deposite
                4 == Bank transfer
                5 == Exit
                """)

            try:
                option = int(input("Enter your choice : "))
            except:
                print("Please enter valid option...!")
                continue

            if option == 1:
                print(f"Your current balance is {balance}")
                print("Thank You For Using This ATM.")
                exit()

            elif option == 2:
                while True:
                    withdraw_amount = int(input("Enter Withdraw Amount : "))
                    if withdraw_amount > balance:
                        print("Insufficient balance in your account. Please try again.")
                    else:
                        balance = balance - withdraw_amount
                        print(f"Your Remaining Balance is : {balance}")
                        time.sleep(3)
                        print("Thank You For Using This ATM.")
                        exit()

            elif option == 3:
                while True:
                    deposite_amount = int(input("Enter Deposite Amount : "))
                    balance = balance + deposite_amount
                    print(f"Your Current Balance is : {balance}")
                    print("Thank You For Using This ATM.")
                    exit()

            elif option == 4:
                while True:
                    account_number = int(input("Enter the Account Number : "))
                    if account_number == account_number_1 or account_number == account_number_2:
                        while True:
                            transfer_amount = int(input("Enter Transfer Amount : "))
                            if transfer_amount > balance:
                                print("Insufficient balance in your account. Please try again.")
                            else:
                                balance = balance - transfer_amount
                                print(f"Your Remaining Balance is : {balance}")
                                print("Thank You For Using This ATM.")
                                exit()
                        break
                    else:
                        print("Invalid Account Number. Please try again.")
                        continue

            elif option == 5:
                print("Thank You For Using This ATM.")
                exit()

        else:
            wrong_pin_count += 1
            if wrong_pin_count == 3:
                print("You have entered wrong PIN 3 times. Please try again after 12 hours.")
                time.sleep(43200)  # Wait for 12 hours
                wrong_pin_count = 0
            else:
                print("Wrong PIN inserted. Please try again.")

atm_simulator()