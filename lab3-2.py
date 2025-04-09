#!/usr/bin/env python3
# -*- coding: utf-8 -*-

N = 1;
open('Output.txt', 'w'); #tworzy plik jeżeli nie istnieje

with open('heme.pdb') as f: # otwiera plik jako f
    linie = f.readlines()   #zczytuje ilość linii


heme = [ l.strip() for l in open('heme.pdb')]  #zczytaj
#print(len(linie))
atomy = [ x.split()[2] for x in heme if x.startswith('ATOM')] #zaczynaj od słowa klucz ATOM
#print(atomy)  #wiadomo 
x = [ x.split()[6] for x in heme if x.startswith('ATOM')] #to samo ale bierze liczbe X z pliku
y = [ x.split()[7] for x in heme if x.startswith('ATOM')]   #analogicznie
z = [ x.split()[8] for x in heme if x.startswith('ATOM')]   #zjadłbym kebaba
#print(atomy[0]+" "+x[0]+" "+y[0]+" "+z[0])

while N < len(linie)-3: #-3 bo 3 linie są zasrane
    with open('Output.txt', 'a') as f:
        f.write(atomy[N]+" "+x[N]+" "+y[N]+" "+z[N] + "\n")
    N = N+1;






######### TODO bo ni chuja nwm co oznaczają dane w OG pliku #################################
######### + pliki otwiera się po 20 razy a raczej to nie dobre novinky ######################