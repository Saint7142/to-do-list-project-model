#User data
account = {
    "user1": {"password":"1234", "balance":10000},
    "user2": {"password":"083434", "balance":12000}
}
#Log in 
while True:
    user = (input("Username: "))
    password = (input("Password: "))
    if user in account and account[user]["password"]==password:
        print("Log in successfully")
        break
    else:
        print("Please Log in again")
#Banking
while True:
    method = (input("Deposit(Press 1), Withdraw(Press 2), End service(Press 3 ): "))
    match method:
        case "1":                
            deposit = int(input("Money Deposited: "))
            account[user]["balance"]+=deposit
            print(f"Total money: {account[user]['balance']:,}")
        case "2":
            withdraw = int(input("Money withdraw: "))
            if account[user]["balance"]>=withdraw:
                account[user]["balance"]-=withdraw
                print(f"Total money: {account[user]['balance']:,}")
            else:
                print("Not enough balance")
        case "3":
            print("End of service")
            break
        case _:
             print("Try again")
