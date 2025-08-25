available_s={
    'Apple':200,
    'Google':180,
    'Tesla':175,
    'Walmart':187,
    'IBM':130,
    'Amazon':156,
    'Unity':96,
    'Microsoft':182
}
stock=input("Enter Stock Name You want to Buy:")
if stock in available_s:
         quantity=int(input("Enter Quantity:"))
         print(f"Your Entered quantity on {stock} Share is:{quantity}")
         opt=input(f"Are you Sure to buy {quantity} shares of {stock}! \n Enter 'yes' or 'YES'to Continue")
         if opt=='yes' or opt=="YES":
           investment=quantity*available_s[stock]
           print(f"Your Investment is:{investment}")
else:
        print(f"We donot have {stock} stock on our Platform") 
with open(r"C:\Users\User\Desktop\Python\CODE ALPHA\stock tracker.txt","a") as inputfile:
        inputfile.write(f"You invested {investment}$ for buying {quantity} shares of {stock}.\n")
        
