#sum digits

#input validity
def input_validity(input1):
    try:
        int(input1)
        return True
    except ValueError:
        return False

#initialize variable
digits_sum = 0       

#get input
number = input("Enter a number:")


#test input validity
if input_validity(number):
    #make calculations
    for digit in number:
        digits_sum+=int(digit)
    #output
    print (digits_sum)
#error message
else:
    print("Invalid input")
