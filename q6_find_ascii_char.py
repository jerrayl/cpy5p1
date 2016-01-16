# find ASCII char

#input validity
def input_validity(input1):
    try:
        int(input1)
        return True
    except ValueError:
        return False

#get input
code = input("Enter an ASCII code:")
#test input validity
if input_validity(code) and 0<=int(code)<=127:
    #output
    print (chr(int(code)))
else:
    #error message
    print("Invalid input")
