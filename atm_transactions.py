 
name="manohar"
password="123"
user_name=input("enter  the user_name:")
password=input("enter the password:")
s='''
1.credit
2.debit
3.mini statement
4.exit
'''
amount=10000
if name==user_name and password==password:
  while True:
     print(s)
     option=int(input("enter the option:"))
     if option==1:
       credit_amount=float(input("enter the amount:"))
       print("amount after credit:",amount+credit_amount)
     elif option==2: 
      debit_amount=float(input("enter the amount:"))
      print("amount after debit:",amount-debit_amount)
     elif option==3:
      print("amount:",amount)
     elif option==4:
        break
else:
      print("incorrect")