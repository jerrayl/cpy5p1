#generate payroll

#input validity
def input_validity(input1,input2,input3):
    try:
        float(input1)
        float(input2)
        float(input3)
        return True
    except ValueError:
        return False
        
#get input
name = input("Enter name:")
hours = input("Enter number of hours worked weekly:")
pay_rate = input("Enter hourly pay rate:")
cpf = input("Enter CPF contribution rate(%):")

#test input validity
if input_validity(hours,pay_rate,cpf):
    #make calculations
    gross_pay = float(pay_rate)*float(hours)
    cpf_contribution = gross_pay*float(cpf)/100
    net_pay = gross_pay-cpf_contribution
    #output
    print ("Payroll statement for " + name)
    print ("Number of hours worked in week: " + hours)
    print ("Hourly pay rate: $ " + pay_rate)
    print ("Gross pay = ${0:.2f}".format(gross_pay))
    print ("CPF contribution at {0}% = ${1:.2f}".format(cpf,cpf_contribution))
    print ("Net pay = ${0:.2f}".format(net_pay))
#error message
else:
    print("Invalid input")
