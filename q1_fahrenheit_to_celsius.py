#farenheit to celcius

#input validity
def input_validity(input1):
    try:
        float(input1)
        return True
    except ValueError:
        return False
        
#get input
farenheit = input("Enter temperature in Farenheit:")

#test input validity
if input_validity(farenheit):
    #make calculations
    celsius = (5/9) * (float(farenheit) - 32)  
    #output
    print ("The temperature in Celcius is {0:.2f} ".format(celsius))
#error message
else:
    print("Invalid input")
