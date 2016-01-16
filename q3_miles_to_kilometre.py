#miles to kilometers

#input validity
def input_validity(input1):
    try:
        float(input1)
        return True
    except ValueError:
        return False

#get input
miles = input("Enter distance in miles:")


#test input validity
if input_validity(miles):
    #make calculations
    kilometers = float(miles)*(1.60934)
    #output
    print ("Distance in kilometers is {0:.3f}".format(kilometers))
#error message
else:
    print("Invalid input")
