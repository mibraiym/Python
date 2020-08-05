'''Problem : If you had deposited a coin on the cryptocurrency exchange that brought 7% fixed profit daily 
for a week, how much would your $ 1000 reach at the end of the 7th day?
Consider using below formula:
PV = Principal Value
FV = Future Value
rate = Interest Rate
days = Number of Periods
FV = PV * (1 + rate/100) ** days
'''

rate = 0.07
pv = 1000
days = 7
fv = (1 + rate) ** days * pv
fv_rounded = str(round(fv, 2))
#answer = "With {}% fixed profit daily my ${} investment will reach ${} at the end of the {}th day.".format(rate, pv, fv_rounded, days)
answer = f"With {rate}% fixed profit daily my ${pv} investment will reach ${fv_rounded} at the end of the {days}th day."

print(answer)

