def pay_calc(num_hrs, hourly_wages, tax_bracket):
    pay_before_tax = hourly_wages * num_hrs
    pay_after_tax = pay_before_tax * (1- tax_bracket)
    return(pay_after_tax)
num_hrs = int(input("enter hours worked: "))
hourly_wages = float(input("hourly wages: "))
tax_bracket = float(input("what is the tax bracket?: "))
print("total take home pay is: ", pay_calc(num_hrs, hourly_wages, tax_bracket))

