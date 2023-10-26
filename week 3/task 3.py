old_pass = input("enter password: ")
new_pass = input("enter a new password between 8 and 12 characters: ")
new_pass2 = input("enter the new password again: ")
if new_pass == new_pass2:
    if len(new_pass) > 7:
        if len(new_pass) < 13:
            print("password is correct length")
            print("new password created")
        else:
            print("not between 8 and 12")
    else:
        print("not between 8 and 12")
else:
    print("passwords did not match")

