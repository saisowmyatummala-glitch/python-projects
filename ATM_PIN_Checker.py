correct_pin = "1234"
for attempt in range (3): 
   pin = input("Enter your PIN: ")
   if pin == correct_pin:
       print("Access Granted!")
       break
   else: 
    print( "Incorrect PIN")
else:
    print("Account Locked!")