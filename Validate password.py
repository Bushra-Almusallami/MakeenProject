import re

string=input("Enter password:")

valid= True

while valid:
    if (len(string)<8 or len(string) >12):
        break
    elif not re.search("[a-z]",string):
        break
    elif not re.search("[A-Z]",string):
        break
    elif not re.search("[0-9]",string):
        break
    elif not re.search("[@#$_]",string):
        break
    elif re.search("\s",string):
        break
    else:
        print("Valid password!")
        valid=False
        break
    
if valid:
    print("The string does not contain a valid password.")
