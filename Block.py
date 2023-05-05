# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 17:55:54 2023

@author: user
"""

class Block:
    def blocking(self,data:list,**kwargs):
        if "multiple" in kwargs.keys():
            m = kwargs["multiple"]
        else:
            m = 10
        
        