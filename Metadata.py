# -*- coding: utf-8 -*-
"""
Created on Sat May  6 11:11:12 2023

@author: echo
"""


class Metadata:
    def add(self,maindata:list,metadata:list):
        n = len(metadata)
        if n > 65535:
            print("\aERROR[Metadata]: The data size is too large.　(data <= 65535)")
            return(None)
        n = list(int.to_bytes(n,2,"big"))
        metadata += n
        res = maindata + metadata
        return(res)
    
    
    
if __name__ == "__main__":
    data = list(range(10))
    meta = [11,12,13]
    res = Metadata().add(data,meta)
    print(res)