#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from rdkit import Chem;
from rdkit.Chem import Descriptors,Crippen , Lipinski,Draw;
import pandas as pd;
import matplotlib.pyplot as plt;


suppl = Chem.SDMolSupplier('test.mol' )    #zczytanie z pliku
molecules = [ mol for mol in suppl if mol is not None ]

def calculate_properties(mol):
    name = mol.GetProp("_Name") if mol.HasProp("_Name") else "Brak Nazwy" #Zczytanie nazwy z pliku jeżeli jej nie ma daje "Brak Nazwy"
    return {    #zwrot z funkcji e.g func nie jest voidem
        'Nazwa' : name,
        'SMILES' : Chem.MolToSmiles(mol) ,  #stworzenie SMILES'a
        'Masa molowa' : Descriptors.MolWt( mol ) ,  # Wyczytanie masy molowej
        ' LogP ' : Crippen.MolLogP ( mol ) ,
        ' Liczba donorow H ' : Lipinski.NumHDonors ( mol ) ,    
        ' Liczba akceptorow H ' : Lipinski.NumHAcceptors ( mol ) ,
        ' Liczba pierscieni ' : Descriptors.RingCount ( mol ) ,
        ' Liczba wiazan rotowalnych ' : Lipinski.NumRotatableBonds ( mol )
        }   #generalnie używanie func z rdkita do zbierania danych z pliku

properties = [ calculate_properties ( mol ) for mol in molecules ]
df = pd.DataFrame ( properties )
print ( df )


plt.hist ( df['Masa molowa'] , bins=20 , edgecolor= 'black' )   #określanie stylu histogramu z tablicy df dla masy Mol
plt.title ( ' Rozklad masy molowej ' )                          #Tytuł
plt.xlabel ( ' Masa molowa [ g/mol ] ' )                        #Labelka dla osi x
plt.ylabel ( ' Liczba czasteczek ' )                            #Labelka dla osi y
plt.show ( );
plt.hist ( df[' LogP '] , bins=20 , edgecolor= 'black' )   #określanie stylu histogramu z tablicy df dla LogP
plt.title ( ' Rozklad LogP ' )                          #Tytuł
plt.xlabel ( ' LogP ' )                        #Labelka dla osi x
plt.ylabel ( ' Liczba czasteczek ' )                            #Labelka dla osi y
plt.show ( );
plt.hist ( df[' Liczba donorow H '] , bins=20 , edgecolor= 'black' )   # --||--
plt.title ( ' Rozklad Liczba donorow H  ' )                          
plt.xlabel ( ' Liczba donorow H  ' )
plt.ylabel ( ' Liczba czasteczek ' )                            
plt.show ( );
plt.hist ( df[' Liczba akceptorow H '] , bins=20 , edgecolor= 'black' )   # --||--
plt.title ( ' Rozklad Liczba akceptorow H  ' )                          
plt.xlabel ( ' Liczba akceptorow H  ' )
plt.ylabel ( ' Liczba czasteczek ' )                            
plt.show ( );
plt.hist ( df[' Liczba pierscieni '] , bins=20 , edgecolor= 'black' )   # --||--
plt.title ( ' Rozklad Liczba pierscieni  ' )                          
plt.xlabel ( ' Liczba pierscieni ' )
plt.ylabel ( ' Liczba czasteczek ' )                            
plt.show ( );
plt.hist ( df[' Liczba wiazan rotowalnych '] , bins=20 , edgecolor= 'black' )   # --||--
plt.title ( ' Rozklad Liczba wiazan rotowalnych  ' )                          
plt.xlabel ( ' Liczba wiazan rotowalnych ' )
plt.ylabel ( ' Liczba czasteczek ' )                            
plt.show ( );


df.to_csv ( 'wynik.csv' , index=False ) #tavlica df > csv

Draw.MolsToGridImage(molecules, legends=[df["SMILES"][i] for i in range(len(molecules))], molsPerRow=4).save("smiles.png")
Draw.MolsToGridImage(molecules, legends=[df["Nazwa"][i] for i in range(len(molecules))], molsPerRow=4).save("nazwy.png")

