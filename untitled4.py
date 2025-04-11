# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 12:41:10 2025

@author: Student
"""
N = 0;
MTemp = []

heme = [ l.strip() for l in open ( 'heme.pdb' ) ]


atomy = [x.split() [ 2 ] for x in heme if x.startswith('ATOM') ]


Xmasy = [ float ( x.split() [ 6 ] ) for x in heme if x.startswith ( 'ATOM' ) ]
Ymasy = [ float ( x.split() [ 7 ] ) for x in heme if x.startswith ( 'ATOM' ) ]
Zmasy = [ float ( x.split() [ 8 ] ) for x in heme if x.startswith ( 'ATOM' ) ]


XmassCenter = sum(Xmasy)/len(Xmasy);
YmassCenter = sum(Ymasy)/len(Ymasy);
ZmassCenter = sum(Zmasy)/len(Zmasy);


slownik = {
    
    "C" : 12,
    "N" : 14,
    "F" : 56,
    "H" : 1,
    "O" : 16
    
    
    }
    
result = [word[0] for word in atomy]
print(result)

while N != len(result):
    
    print(slownik[result[N]])
    MTemp.append( slownik[result[N]])
    N = N+1;

print(sum(MTemp))

MasaAtomowa = sum(MTemp);
x_cm = sum( [Xmasy[i]*MTemp[i] / MasaAtomowa for i in range ( len(atomy) )] )
y_cm = sum( [Ymasy[i]*MTemp[i] / MasaAtomowa for i in range ( len(atomy) )] )
z_cm = sum( [Zmasy[i]*MTemp[i] / MasaAtomowa for i in range ( len(atomy) )] )

print(x_cm);
print(y_cm);
print(z_cm);


with open('Wynik.txt','w') as wynik:
    wynik.write("Centrum Geometryczne : "+" |X|: "+str(XmassCenter)+" |Y|: "+str(YmassCenter)+" |Z|: "+str(ZmassCenter)+ "\n");
    wynik.write("Masa Atomowa to: "+str(MasaAtomowa) +" \n");
    wynik.write("Centrum Wagowe: " + "|X|: "+str(x_cm)+" |Y|: "+str(y_cm) + " |Z|: "+ str(z_cm)+  " \n");
    wynik.write('Struktura zawiera {} atomów:\n'.format(len(atomy)))
    for i in atomy:
        wynik.write('{}\n'.format(i));
   