# Basic python code that calculates payment depends on minutes spoken
a,b,c=input("Minute spoke:").split()
a=float(a)
b=float(b)
c=float(c)
t=a*60+b+c/60
pay=0.00
tax=0.00
if t<0:
    print("No minutes talked")
elif t<=30:
    pay=30*0.9
    tax=30*0.9*0.08
elif t<=80:
    pay=t*0.9
    #base*0.9 is 27 and t-27 isn't meaningful
    tax=(27*0.08)+((t-27)*0.18)
elif t<=130:
    pay=t*0.75
    tax=pay*0.18
else:
    pay=t*0.6
    #this taxes calculation is the best and true
    tax=(27*0.08)+((pay-27)*0.18)
tot=pay+tax
print("Total pay is: %.2f TL"%pay)
print("Taxes:%.2f TL"%tax)
print("Total pay is: %.2f TL"%tot)
