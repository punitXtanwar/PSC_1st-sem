
Number=int(input("Enter a Number"))
last_digit=Number%8
print(last_digit)




Number=int(input("Enter a Number"))
if Number%2==0:
   print("Number is Even")
else:
   print("Number is odd")       

# # #check whether a Number is divisible by 3 and 5
Number=int(input("Enter a Number"))
if Number%3==0 and Number%5==0:
   print("Number is divisible by 3 and 5")
if Number%3==0 and Number%5!=0:
   print("Number is divisible by 3 but not 5")
if Number%5==0 and Number!=0:
   print("Number is divisible by 5 but not 3")
if Number%3!=0 and Number%5!=0:
   print("Number is neither divisible by 3 nor 5")    




#user inputs one of the colour red,green,yellow based on program you should print: 'stop' for Red ,'get ready' for yellow and 'Go' for green

colour=input("Enter a colour")
if colour=="RED":
   print("STOP")
if colour=="YELLOW":
   print("Get Ready")
if colour==("GREEN"):
   print("Go")            