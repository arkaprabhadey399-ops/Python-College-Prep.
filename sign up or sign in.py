"""CODE FOR SIGN UP OR SIGN IN TO PUBLIC SERVICE PORTAL BY KAUSIK DEY"""
print("=====================WELCOME TO PUBLIC SERVICE PORTAL===================")
print("SIGN UP OR SIGN IN TO CONTINUE")
print("1. SIGN UP")
print("2. SIGN IN")    
option = int(input("ENTER YOUR OPTION: "))
if option == 1:
    print("SIGN UP")
    name = input("ENTER YOUR NAME: ")
    email = input("ENTER YOUR EMAIL: ")
    password = input("ENTER YOUR PASSWORD: ")
    COMFIRM_PASSWORD = input("CONFIRM YOUR PASSWORD: ")
    if password == COMFIRM_PASSWORD:
        print("SIGN UP SUCCESSFUL")
        print("1. VIEW PROFILE")
        print("2. LOG OUT")
        option = int(input("ENTER YOUR OPTION: "))
        if option == 1:
            print("VIEW PROFILE")
            print("NAME: ", name)
            print("EMAIL: ", email)
        elif option == 2:
            print("LOG OUT")
            print("YOU HAVE BEEN LOGGED OUT SUCCESSFULLY")
            print("THANK YOU FOR USING PUBLIC SERVICE PORTAL")
        else:
            print("INVALID OPTION")
    else:
        print("PASSWORDS DO NOT MATCH")
        
elif option == 2:
    print("SIGN IN")
    email = input("ENTER YOUR EMAIL: ")
    password = input("ENTER YOUR PASSWORD: ")
    if email == "example@gmail.com" and password == "123456":
        print("SIGN IN SUCCESSFUL")
        print("Welcome back, Example Name!")
        print("1. VIEW PROFILE")
        print("2. LOG OUT")
        option = int(input("ENTER YOUR OPTION: "))
        if option == 1:
            print("YOUR PROFILE")
            print("NAME: Example Name")
            print("EMAIL: example@gmail.com")
        elif option == 2:
            print("LOGGING OUT.........")
            print("YOU HAVE BEEN LOGGED OUT SUCCESSFULLY")
            print("THANK YOU FOR USING PUBLIC SERVICE PORTAL")
        else:
            print("INVALID OPTION")
    else:
        response = "INVALID EMAIL OR PASSWORD"
        print(response)
        print("PLEASE TRY AGAIN")
                                                                                                                                               

#==================Built after Lec-2===========================#