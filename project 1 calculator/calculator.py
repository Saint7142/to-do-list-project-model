#input
#log in 
while True:
    username = str(input("Username: "))
    password = str(input("password: "))
    if username=="Pongphon" and password=="1234":
        print("Log in succesfully")
        break
    else: 
        print("Please Log in again")
#calculation selection
selection = str(input("If you want to use calculation(press 1), end program(press 2)"))
match selection:
    case "1":
        method = str(input("pls type any method(+,-,/,*): "))
        match method:
            case "+":
                fnumber = int(input("first number: "))
                snumber = int(input("second number"))
                result = fnumber+snumber
                print(fnumber, "+", snumber, "=", result)
            case "-":
                fnumber = int(input("first number: "))
                snumber = int(input("second number"))
                result = fnumber-snumber
                print(fnumber, "-", snumber, "=", result)
            case "/":
                fnumber = int(input("first number: "))
                snumber = int(input("second number"))
                result = fnumber/snumber
                if snumber==0:
                    print("Can't divinded by zero")
                else:
                                                print(fnumber, "/", snumber, "=", result)
            case "*":
                fnumber = int(input("first number: "))
                snumber = int(input("second number"))
                result = fnumber*snumber 
                print(fnumber, "*", snumber, "=", result)
    case "2":
        print("End program")
    case _:
        print("End program")
        