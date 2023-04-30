# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 00:51:45 2023

@author: user
"""

from random import randint

class Sub:
    # Check whether the input argument is an integer and handle the exception if it is different.
    def set_multiple(self,m):
        # multiple
        try:
            if type(m) != int():
                print("ERROR[Pad]:'multiple' input only int.　It automatically set the value to 10.")
                m = 10
        except:
            m = 10
        return(m)
        
    # Decide the length of the bytes to add.
    def set_pad_length(self,data:list,m:int):
        a = len(data)
        b = a + (m - a % m)
        x = b - a
        return(x)
    
    # Generates an array of the specified length.
    # The end contains the length of the generated data.
    # By default, elements are created randomly, but it is also possible to create them with all zeros.
    def generate_pad_array(self,length:int,**kwargs):
        if "random" in kwargs.keys():
            if kwargs["random"] == False:
                res = [i*0 for i in range(length-1)]
                res.append(length)
        else:
            res = [(i*0)+randint(0,255) for i in range(length-1)]
            res.append(length)
        return(res)


# Main
class Pad:
    def __init__(self):
        self.help = """
        Adjusts the size of the bytes.
        The default is to fit to multiples of 10.
        """
    
    def add(self,data:list,**kwargs):
        m = Sub.set_multiple(kwargs["multiple"])
        
    def remove(self,data:list,**kwargs):
        m = Sub.set_multiple(kwargs["multiple"])
        
if __name__ == "__main__":
    print(Sub().generate_pad_array(10))
    