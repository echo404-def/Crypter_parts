# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 17:55:54 2023

@author: echo
"""

class Block:
    def blocking(self,data:list,**kwargs):
        if "multiple" in kwargs.keys():
            m = kwargs["multiple"]
        else:
            m = 10
        if len(data) % m != 0:
            print("\aERROR[Block]: Incorrect multiple value")
            return(None)
        res = list()
        for i in range(len(data)//m):
            i = data[:10]
            data = data[10:]
            res.append(i)
        return(res)
            
    
    def joining(self,data:list):
        if type(data) != list():
            print("\aERROR[Block]: Incorrect arguments.")
            return(None)
        res = list()
        for i in data:
            res += i
        return(res)
    
    
if __name__ == "__main__":
    data = list(range(31))
    r = Block().blocking(data)
    print(r)
    r2 = Block().joining(r)
    print(r2)