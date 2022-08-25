# asking for hours
hrs = input("Enter Hours:")
h = float(hrs)

# asking for rate
rate = input('Enter hourly rate:')
r = float(rate)

# 2-way branching
# |
# ---less than equal to 40 -> rate is original rate
# ------more than 40 ->  rate is 1.5 times original rate

if(h<=40):
    pay = h * r
    print(pay)
else:
    extraHours = h - 40;
    pay = ((h-extraHours) * r) + (extraHours * r * 1.5)
    print(pay)