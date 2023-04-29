# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 00:51:45 2023

@author: user
"""

class Sub:
    def set_multiple(self,m):
        # multiple
        try:
            if type(m) != int():
                print("ERROR[Pad]:'multiple' input only int.　It automatically set the value to 10.")
                m = 10
        except:
            m = 10
        return(m)
        
    def set_pad_length(self,data:list,m:int):
        a = len(data)
        b = a + (m - a % m)
        x = b - a
        return(x)


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
    data = list(range(61))
    m = 10
    print(Sub().set_pad_length(data, m))
    