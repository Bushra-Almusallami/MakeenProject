string=input("Enter string in format (xxx)xxx-xxxx:")
valid=len(string) ==13
position=0
while valid and position < len(string):
    if position == 0:
        valid = string[position]=="("
    elif  position == 4:
        valid = string[position]==")"
    elif  position == 8:
        valid = string[position]=="-"
    else:
        valid = string[position].isdigit()
    position = position +1
    
if valid:
    print("The string contain a valid phone number.")
else:
    print("The string does not contain a valid phone number.")

