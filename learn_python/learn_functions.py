def myfunc2(A, B):
    if A >= 10:
        if A > B:
            if A == 100:
                print('A is greater or equal to 10')
                print('A is less than B')
            else:
                print(f'A = {A}')
                
myfunc2(23,20)

def sum_func(*args):
    final_num = 0
    for num in args:
        final_num += num # adds each argument to final_num
    return(final_num)

print (sum_func(2,3,4,8,9))

import math

def Area_of_circle(radius):
    Area = math.pi * radius**2
    return (Area)

print(Area_of_circle(8))

myfunc2(100,20)

def sums(*args, **kwargs):
    total = 0
    for num in args: # iterate over the numbers in the positional argument
        total += num  # Summing up all values in keyword arguments (values of nums1, nums2, etc.)
    for k,v in kwargs.items(): #iterate over keyword arguments
        total += v
    return (total)

print (sums(1, 2, 3, 4, nums1= -4, nums2= 8))


def filter_even_number(*num):
    my_func = lambda x: x%2 == 0
    even_number = []
    for i in num:
        if my_func(i):
            even_number.append(i)
    return(even_number)
    
print(filter_even_number(2,4,5,3,8,7,90,78,67,6,0,100))

def filter_odd_number(*num):
    odd_number = list(filter(lambda x : x % 2 != 0, num))
    return (odd_number)
    
    
print(filter_odd_number(2,4,5,3,8,7,90,78,67,6,0,100))   


def sales_price (price):
    discounted_price = (lambda x: x - (x*0.05))(price)
    return (discounted_price)

print(sales_price(90000))


def apply_discount(prices, discount_percentage):
    discount = lambda price: price * (1 - discount_percentage / 100)
    return [discount(price) for price in prices]

prices = [100, 200, 300, 400, 500]
discount_percentage = 20
discounted_prices = apply_discount(prices, discount_percentage)
print(discounted_prices)


