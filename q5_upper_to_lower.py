# upper to lower

#get input
lower = input("Enter an uppercase letter:")

#convert letter


#test input validity
if len(lower)==1:
    #get ascii value
    ascii_value = ord(lower)
    #test if a uppercase letter was entered
    if 65<=ascii_value<=90:
        #convert to lowercase
        upper = chr(ascii_value+32)
        #output
        print (upper)
    else:
        #error message
        print("Invalid input")
else:
    #error message
    print("Invalid input")
