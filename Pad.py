# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 00:51:45 2023

@author: echo
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
        f = Sub()
        if "multiple" in kwargs.keys():
            m = f.set_multiple(kwargs["multiple"])
        else:
            m = 10
        length = f.set_pad_length(data, m)
        pad = f.generate_pad_array(length)
        res = data + pad
        return(res)
        
    def remove(self,data:list,**kwargs):
        f = Sub()
        if "multiple" in kwargs.keys():
            m = f.set_multiple(kwargs["multiple"])
        else:
            m = 10
        length = f.set_pad_length(data, m)
        res = data[:data[-1]*-1]
        return(res)
        
