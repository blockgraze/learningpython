hrs = input("Enter Hours: ")
if float(hrs) < 10 :
    hrs = 'Please Contact Admin'
    print(hrs)
    exit()
rte = input("Enter Rate: ")
prt = float(hrs) * float(rte)
if prt < 100 : prt = 'Too Low for Payment'
print("Pay for Period:", prt)
