#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
    Created on Mon Jan 7 23:31:13 2024
    Title   :   Encryption-Decryption
    @author :   Poushali Chattopadhyay
"""

def make_type(key:int) -> callable: 
    # It returns a function that, when given a character, shifts the character by the provided integer key value. 
    return lambda p : chr(32 + (ord(p)+key)%127) if (ord(p)+key)%127 < 32 else chr((ord(p)+key)%127)

option:str = ''  # determines whether the program will continue or not 

while option!='e' and option!='E':
    msg:str = input("\nEnter the Text : ")
    while True:
        try : 
            key:int = int(input("Enter the key :"))
            break
        except: 
            print ("Wrong Input! Should be an integer. Try Again!")

    while True : 
        encrypt_type = input("Choose mode.. Encrypt[e/E] Decrypt[d/D] : ")
        if encrypt_type in ['e','E','D','d']:break
        else:print('Wrong choice!' )         

    if encrypt_type == 'e' or encrypt_type == 'E':
        # In encryption, the key value is passed through the shift function to determine the shifting of characters.
        print("Encrypted message: "+"".join(map(make_type(key),msg)))
    elif encrypt_type == 'd' or encrypt_type == 'D' : 
        # For decryption, the key value is negated, and then passed through the shift function to reverse the character shifting process. 
        print("Encrypted message: "+"".join(map(make_type(-1*key),msg)))

    option= input("\nEnter Choice Continue[c/C]  Exit[e/E]:")




