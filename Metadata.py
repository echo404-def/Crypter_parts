# -*- coding: utf-8 -*-
"""
Created on Sat May  6 11:11:12 2023

@author: echo
"""


class Metadata:
    # Add metadata after the main data.
    # The last two bytes of metadata represent the data size.
    def add(self,maindata:list,metadata:list):
        n = len(metadata)
        # Displays an error if the data size is too large and returns None.
        if n > 65535:
            print("\aERROR[Metadata]: The data size is too large.　(data <= 65535)")
            return(None)
        n = list(int.to_bytes(n,2,"big"))
        metadata += n
        res = maindata + metadata
        return(res)
    
    # Returns main data and metadata in dictionary type.
    def remove(self,data:list):
        n = int.from_bytes(bytes(data[-2:]),"big")
        meta = data[-(n+2):-2]
        data = data[:-(n+2)]
        res = {"main":data,"meta":meta}
        return(res)

