# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def mul5or3():
    sum=0
    for i in range(3,1000,1):
        if(i%3==0 or i%5==0):
            sum+=i 
    print("the total sum is ",sum)
        
            
        