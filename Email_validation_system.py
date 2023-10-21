email = input("Enter Your Email : ")
k = 0
j = 0
d = 0
if len(email) >= 6:
    if email[0].isaplha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4]==".") ^ (email[-3]=="."):
                for i in email:
                    if i == i.isspace():
                        k = 1
                    elif i.isaplha():
                        if i == i.upper():
                            j = 1
                    elif i.isdigit():
                        print("Valid Email")
                        continue
                    else :
                        d = 1 
                if k == 1 or j == 1 or d == 1:
                    print("Invalid Email Address !")        
            else:
                print("Invalid Email Address !")
        else:
            print("Invalid Email Address!")
    else:
        print("Invalid Email Address!")
else:
    print("Invalid Email Address!")