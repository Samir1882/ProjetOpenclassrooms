#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 14:36:04 2018

@author: karkar
"""
import uansi 
###Exercice1: Nombres parfaits et amicaux

def somdiv(n):
    Somme = 0
    for i in range(1,n):
        if n%i == 0:
            Somme = Somme + i
    return Somme

def parfait(n):
    return somdiv(n)==n

def Parfaits(N):
    l=[]
    for n in range(1,N):
        if parfait(n):
            l.append(n)
    return l

def amicaux(n):
    l=[]
    for i in range(1,n):
        s = somdiv(i)
        for j in range (i+1,n):
            if s == j  and somdiv(j) == i:
                l.append([i,j])
    return l

def amicaux2(n):
    l=[]
    for i in range (1,n):
        s = somdiv(i)
        if somdiv(s)==i and i<s<n:
            l.append ([i,s])
    return l

###Exercice2: Nombres chanceux
def premier(n):
    if n==0 or n==1:
        return False
    if n==2:
        return True
    d=2
    while d**2<n+1:
        if n%d==0:
            return False
        d=d+1
    return True

def chanceux(n):
    for i in range(0,n-1):
        if not premier (n+i**2+i):
            return False
    return True

def ListeChanceux(N):
    l=[]
    for n in range (2,N):
        if chanceux(n):
            l.append(n)
    return l