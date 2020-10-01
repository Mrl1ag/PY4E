# 3.1 Write a program to prompt the user for hours and rate per hour using
# input to compute gross pay. Pay the hourly rate for the hours up to 40 and
# 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours
# and a rate of 10.50 per hour to test the program (the pay should be 498.75).
# You should use input to read a string and float() to convert the string to a
# number.


hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Erro, por favor insira um valor numérico")
    quit()
if h <= 40:
    gp = h * r
    print("Pay me:", gp)
elif h > 40:
    oh = (40 * r) + ((r * 1.5) * (h - 40))
    print("You better have my", oh)
