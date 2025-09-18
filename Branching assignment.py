electricity = int(input("Enter the number of KW used"))
if electricity <= 1000:
    totalBill = (7.633/100)*electricity
    print("The total electricity cost is $",cost )
elif hours > 1000:
    totalBill2 = ((9.259/100)*(hours-1000)) + (7.633/100)* 1000
    print("The total electricity cost is $",totalBill2)
else:
    print("The number you entered must be greater than 0")