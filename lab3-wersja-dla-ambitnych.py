#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import os

data = os.path.abspath('IR.txt');
x_vals = []
y_vals = []



def draw_ir(a):
    with open(a) as f:      #otwórz plik jako F
        for line in f:      #loop na każdą linie w F
            try:            
                x, y = map(float, line.strip().split()) #Try sprawdza czy coś jest floatem a jak nie jest to wykurwia
                x_vals.append(x)                        #a jak jest to wpierdala do tablicy
                y_vals.append(y)
            except ValueError:
                    continue
    
    
   

    plt.plot(x_vals, y_vals) 
    plt.ylim( 0, np.max(y_vals)+1) # to jest ta cała część dla specjalnych inaczej wsm można dać +1 aby ładnie wyglądało
    plt.grid(True)
    plt.show()

draw_ir(data);