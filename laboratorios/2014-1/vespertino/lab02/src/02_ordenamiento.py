#!/usr/bin/env python
# -*- coding: utf-8 -*-
#L=[4,8,36,45,74,10,1,2,9,18,37]
L=[-14,20,8,-2000,6.9]
def ordenamiento(lista):
    for minimo in range(len(L)):
        for j in range(minimo+1,len(L)):
            if L[j] < L[minimo]:
                L[j],L[minimo]=L[minimo],L[j]
    return lista
print(ordenamiento(L))
