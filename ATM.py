
# Balance initial in an account is 50k
Balance = 50000
withdraw_Amount = 0

# transfer record
account_Number = 0
amount_Transfer = 0

# recharge record
recharge_No = 0
amount_Recharge = 0

cont = 'y'
while cont == 'y':

    print("------------------== ATM System ==----------------")
    print("Press ‘b’ to check balance")
    print("Press ‘w’ to withdraw")
    print("Press ‘t’ to transfer")
    print("Press ‘r’ to recharge mobile balance")
    print("Press ‘s’ to print the transaction summary")

    # taking input from user
    action = input("Enter key: ")

    if action == 'b':
        print("-->> Your Balance: ", Balance)
        print("****** Thanks for using our ATM System **********")
        cont = input("continue (y/n): ")

    elif action == 'w':
        print("-->> Your Balance: ", Balance)
        print("*** Withdraw ***")
        withdraw_Amount = int(input("Enter amount: "))

        if withdraw_Amount <= 20000:
            Balance = Balance - withdraw_Amount
            print("-->> Your Remaining Balance: ", Balance)
        else:
            print("Sorry max limit for withdrawal is: 20,000")
            print("-->> Your Remaining Balance: ", Balance)

        print("****** Thanks for using our ATM System **********")
        cont = input("continue (y/n): ")

    elif action == 't':
        print("-->> Your Balance: ", Balance)
        print("*** Transfer ***")
        account_Number = int(input("Enter Account No.: "))
        amount_Transfer = int(input("Enter amount: "))

        if amount_Transfer <= 20000:
            print("Amount transfer against Account No. ", account_Number)
            Balance = Balance - amount_Transfer
            print("-->> Your Remaining Balance: ", Balance)
        else:
            print("Sorry max limit for transfer is: 20,000")
            print("-->> Your Remaining Balance: ", Balance)

        print("****** Thanks for using our ATM System **********")
        cont = input("continue (y/n): ")

    elif action == 'r':
        print("-->> Your Balance: ", Balance)
        print("*** Recharge Mobile Balance ***")
        recharge_No = int(input("Enter recharge mobile No. : "))
        print("Recharged against mobile No. ", recharge_No)
        amount_Recharge = int(input("Enter amount: "))
        Balance = Balance - amount_Recharge
        print("-->> Your Remaining Balance: ", Balance)
        print("****** Thanks for using our ATM System **********")
        cont = input("continue (y/n): ")

    elif action == 's':
        print("-->> Your Balance: ", Balance)
        print("*** Transaction summary ***")
        print("Withdraw Amount: ", withdraw_Amount)
        print("Transferred Amount: ", amount_Transfer, "Against AccountNo. : ", account_Number)
        print("Recharging Amount: ", amount_Recharge, "Against mobile No. :", recharge_No)
        print("****** Thanks for using our ATM System **********")
        cont = input("continue (y/n): ")

    else:
        print("Sorry! you entered invalid choice")
        cont = input("continue (y/n): ")

print("****** Thanks for using our ATM System **********")
