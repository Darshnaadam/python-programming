email = input(" Enter your Email: ")
k, j, d = 0, 0, 0
if len(email) >= 6:  # Email should not be less than 6 words
    if email[0].isalpha():  # first letter in Email should be alphabet only
        # there should be "@" and only one "@" in email
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == ".") ^ (email[-3] == "."):
                for i in email:
                    if i == i.isspace():
                        k = 1
                    elif i == i.isalpha():
                        if i == i.upper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i == "." or i == "@" or i == "_":
                        continue
                    else:
                        d = 1
                if k == 1 or j == 1 or d == 1:
                    print("wrong Email 5")
                else:
                    print("Right Email")
            else:
                print('Wrong Email 4')
        else:
            print('Wrong Email 3')
    else:
        print('Wrong Email 2')
else:
    print('Wrong Email 1')
