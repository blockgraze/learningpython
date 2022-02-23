hrsinput = input("Enter Hours: ")
rateinput = input("Enter Rate: ")

#define rate and OT rate below
ratebase = float(rateinput)
rateot = (ratebase * 1.5)

#define hours and OT below
hrsfloat = float(hrsinput)
if hrsfloat > 40 :
    hrsot = (hrsfloat % 40)
    otpay = hrsot * rateot
    hrsfloat = 40

basepay = hrsfloat * ratebase

print((basepay) + (otpay))
