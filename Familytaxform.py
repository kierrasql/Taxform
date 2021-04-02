#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Introducting Families to Tax Form

print("Welcome to the Family Tax Form")
 
# Asking for user input

print("Wages, salaries, and tips earned by Husband:$")
husbandanswer= int(input("Fill in:"))
print("Wages, salaries, and tips earned by Wife:$")
wifeanswer= int(input("Fill in:")) 
print ("Bonus earned by the family combined:$")
familybonus= int(input("Fill in:"))

#Display yearly income for family

print("This is your yearly income:$")
yearlyincome=print(husbandanswer + wifeanswer+ familybonus)
yearlyincome=(husbandanswer + wifeanswer+ familybonus)

#Standard Deductable and making yearlyincome int
standard= 5000
yearlyincome=int(yearlyincome)


print("This is your Taxable Income:$")

#Taxable Income is yearlyincome substracted by standard deductable 

Taxableincome= int(yearlyincome) - int(standard)
print("You balance is now: $" + str(Taxableincome) + ".") 

#If statement 

if standard>yearlyincome:
  print("-0-")

print ("Federal income tax withheld from paychecks for Husband")

incometaxhusband=int(input("Fill in:$"))

print("Federal income tax withheld from paychecks for Wife:$")
incometaxwife=int(input("Fill in:"))

print("These are your total payments and credits:$")
paycredits=print(incometaxhusband + incometaxwife)
paycredits=(incometaxhusband+incometaxwife)

print("Your Federal Tax is:$")
Federaltax=print(Taxableincome * 0.28)
Federaltax=(Taxableincome * 0.28)

print("Property Tax to be owed?")
propertytax=int(input("Fill in:$"))
                
owed=print("Tax Owed is $", Taxableincome + propertytax)
owed=(Taxableincome+propertytax)

print("Total Tax:$",owed + Federaltax)

TotalTax=(owed + Federaltax)

if result>paycredits:
    print("The amount you have to pay:")
    
    
if result<paycredits:
    print("The amount you overpaid:")

result=print(TotalTax-paycredits)
result=(TotalTax-paycredits)

print("Thank you!")


# In[ ]:




