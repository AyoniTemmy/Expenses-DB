### Write a Python program that asks the user for their age
#  and determines their age group based on the following criteria:

Age = float(input("How old are you: "))

if 0 <= Age < 13:
    print('Child')
elif 13 <= Age < 20:
    print('Teenager')
elif 20 <= Age < 64:
    print( 'Adult'  )
else:
    print('Senior')

Username = input('What is your username?')
Password = input('What is your password?')

if Username == "admin" and Password == '1234':
    print('login successful')
else:
    print('login unsuccessful')


##Write a program that calculates the discount on a product. 
# If the product price is above $100, the user gets a 20% discount. 
# If the product price is between $50 and $100, the user gets a 10% discount. 
# Otherwise, no discount is given.

Price = float(input('Sales Price _$'))

if Price > 100:
    Discount = 0.20
elif 50 <= Price <= 100:
    Discount = 0.10
else:
    Discount = 0
Sales_Price = Price - (Price * Discount)
print(Sales_Price)


Grade = input('Student grade___')
School_Fees = 1000000

if Grade =='A':
    Discount_ = 0.20
elif Grade == 'B':
    Discount_ = 0.10
else:
    Discount_ = 0

Taiwo_School_Fees = (School_Fees - (School_Fees* Discount_))
print(Taiwo_School_Fees)

for i in range(1,20):
    if i%2 != 0:
        print(i)
        
        
students = [“Ade", “Bashir”, “Celine”, “David”, “Rendani”]
print (student(4))
