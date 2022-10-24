import numpy as np
import pandas as pd


#Zadanie 1

data = pd.read_csv('president_heights.csv')
heights = np.array(data['height(cm)'])

print("\nZadanie 1")
print("Mean height:       ", np.mean(heights))
print("Standard deviation:", np.std(heights))
print("Minimum height:    ", heights.min())
print("Maximum height:    ", heights.max())

print("25th percentile:   ", np.percentile(heights, 25))
print("Median:            ", np.median(heights))
print("75th percentile:   ", np.percentile(heights, 75))


#Zadanie 2

dane2 = np.genfromtxt('Zadanie_2.csv', delimiter=';')

print("\nZadanie 2")
print("Wektory wlasne macierzy: \n", np.linalg.eig(dane2))
print("Wartosci wlasne macierzy: \n", np.linalg.eigvals(dane2))
print("Macierz odwrotna: \n", np.linalg.inv(dane2))


#Zadanie 3

rainfall = pd.read_csv('Seattle2014.csv')['PRCP'].values
inches = rainfall / 254.0  # 1/10mm -> inches

print("\nZadanie 3")
print("Number days without rain:      ", len(inches[inches == 0]))
print("Number days with rain:         ", len(inches[inches > 0]))
print("Days with more than 0.5 inches:", len(inches[inches > 0.5]))
print("Rainy days with < 0.2 inches  :", len(inches[(inches < 0.2) & (inches > 0)]))
print("Median precip on rainy days in 2014 (inches):   ", np.median(inches[inches > 0]))
print("Median precip on summer days in 2014 (inches):  ", np.median(inches[172:262]))
print("Maximum precip on summer days in 2014 (inches): ", np.max(inches[172:262]))
print("Maximum precip on non-summer days in 2014 (inches): ", np.max(inches[not 172:262]))
print("Median precip on non-summer rainy days (inches): ", np.median(inches[not 172:262][inches[not 172:262] > 0]))


#Zadanie 4

A = [0,3,2,5]
B = [0,3,1,4]
A = np.array([0,3,2,5])
B = np.array([0,3,1,4])
a = 4

print("\nZadanie 4")
print("Suma wektora A i wektora B: ", A + B)
print("Roznica wektora A i wektora B: ", A - B)
print("Pomnozenie wektora A przez skalar a: ", A * a)
print("ILoczyn skalarny wektora A i wektora B: ", np.dot(A, B))
print("Dlugosc wektora B: ", np.linalg.norm(B))