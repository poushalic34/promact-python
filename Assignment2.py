#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
    Created on Wed Jan 9 03:15:52 2024
    Title   :   Inventory System
    @author :   Poushali Chattopadhyay 
"""
#A class representing product information with attributes for name, price, quantity, and type.
class Product (object):
    def __init__(self, name, price, quantity, type):
        super().__init__()
        self.name = name 
        self.price = price
        self.quantity = quantity
        self.type = type
#Creates a list containing Product objects to represent diverse vegetables, each with its specific details.
ProductList = [
    Product('lettuce',    10.5,  50,  'Leafy green' ),
    Product('cabbage',    20,    100, 'Cruciferous' ),
    Product('pumpkin',    30,    30,  'Marrow'      ),
    Product('cauliflower',10,    25,  'Cruciferous' ),
    Product('zucchini',   20.5,  50,  'Marrow'      ),
    Product('yam',        30,    50,  'Root'        ),
    Product('spinach',    10,    100, 'Leafy green' ),
    Product('broccoli',   20.2,  75,  'Cruciferous' ),
    Product('garlic',     30,    20,  'Leafy green' ),
    Product('silverbeet', 10,    50,  'Marrow'      )]
#Looks for a product in the provided product_list by matching the product name and returns the first matching product found.
def search_by_name(pr_list,name):
    for p in pr_list:
        if p.name == name:
            return p
#Displays the details of the specified product, presenting information such as name, price, quantity, and type.
def disp(p):
    print(f"Product({p.name},{p.price},{p.quantity},{p.type})")
#Determines the overall quantity of products in the provided productList.
def summation(pList):
    return sum([p.quantity for p in pList])
# Displays the total number of products in the list.
print("Total Count of Products {total_product(ProductList)}")
# Adds a new product to the list, then prints the entire list of products along with the total count of products as an integer.
ProductList.append(Product('Potato',10, 50, 'Root'))
for pr in ProductList: disp(pr) 
print("Total number of Products = {summation(ProductList)}")
# Displays the details of all products in the list that have the type "Leafy green."
for p in ProductList :
    if p.type == 'Leafy green':
        print(p)
# Iterates through ProductList, removes any product with the name 'garlic', and then prints the total number of products.
for product in ProductList:
    if product.name == 'garlic': 
        ProductList.remove(product)
print(f"Total number of Products = {total_product(ProductList)}")
# Retrieves the quantity of cabbages from ProductList and prints the total number of cabbages.
cabbages = [product.quantity for product in ProductList if product.name == 'cabbage'][0]
print(f"Total cabbages will be {cabbages} ")
# Calculates the total cost by summing the prices of lettuce, double the price of zucchini, and broccoli from ProductList.
cost = (search_by_name(ProductList,'lettuce').price 
        +search_by_name(ProductList,'zucchini').price * 2
        +search_by_name(ProductList,'broccoli').price )
print ( f'Total Cost will be {cost}')


