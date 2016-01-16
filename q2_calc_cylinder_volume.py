#calc cylinder volume

#import value of pi
from math import pi

#input validity
def input_validity(input1,input2):
    try:
        float(input1)
        float(input2)
        return True
    except ValueError:
        return False
        
#get input
radius = input("Enter radius of cylinder:")
length = input("Enter length of cylinder:")


#test input validity
if input_validity(radius,length):
    #make calculations
    area = float(radius) * float(radius) * pi
    volume = area * float(length)   
    #output
    print ("The area of the cylinder is {0:.2f} and its radius is {1:.2f} ".format(area,volume))
#error message
else:
    print("Invalid input")
