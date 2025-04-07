import matplotlib.pyplot as plt
N = 0;tablica = [0];a = 0;b = 1;wynik = 0;
while N != 50:

    wynik = a+b;
    a = b;
    b = wynik;
    tablica.append(wynik);
    #print(tablica[N]);
    N = N+1;
plt.plot(tablica);
plt.show;
    