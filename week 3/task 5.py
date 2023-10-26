BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

while True:
    old_pass = input("enter password: ")
    new_pass = input("enter a new password between 8 and 12 characters: ")
    new_pass2 = input("enter the new password again: ")
    if new_pass == new_pass2:
        if len(new_pass) > 7:
            if len(new_pass) < 13:
                if new_pass not in BAD_PASSWORDS:
                    print("password is correct length")
                    print("new password created")
                    break
                else:
                    print("this is a poor password")
            else:
                print("not between 8 and 12")
        else:
            print("not between 8 and 12")
    else:
        print("passwords did not match")
