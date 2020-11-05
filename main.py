import numpy as np
import matplotlib.pyplot as plt

#initializing variables
data = []
k = 0

"""
First task DAC
"""
print("DAC: ")
with open("DAC.txt") as f:
    for line in f:
        buf = line.split('        ')
        if (k == 0):
            buf[0] = buf[0][3:]
            k+=1
        data.append([float(x) for x in buf])
data = np.array(data)
data = data.transpose()
#plt.plot(data[0], data[1])
#plt.grid('True')
#plt.show()
#print(data[0])
#print(data[1])
#определение ошбки мастаба + индекса у нуля
itemindex = np.where(data[0]==0)
#print(itemindex)
#print(np.max(data[1]))
print("Zero error is ", 100*data[1][itemindex[0][0]]/np.max(data[1]), "%")
#убили ошибку нуля
data[1] = data[1] - data[1][itemindex[0][0]]
#plt.plot(data[0], data[1])
#plt.show()
#ошибка масштаба

#интегральная ошибка, т.е. максимальное отклонение от идеальной кривой
fp, residuals, rank, sv, rcond = np.polyfit(data[0], data[1], 1, full=True)
#print(fp, residuals, rank, sv, rcond)
f = np.poly1d(fp)
print("Integ error = ", 100*np.max(np.abs(f(data[0]) - data[1]))/np.max(data[1]), "%")

#дифференциальная ошибка
Dif = data[1][1:] - data[1][0:-1]
meanDif = np.mean(Dif)
maxDif = np.max(np.abs(Dif - meanDif))
print("Dif error = ", maxDif/meanDif,"LSB")
#гистограмма для дифференциальной ошибки
#plt.hist(Dif, bins = 10)
#plt.show()


"""
Second Task ADC
"""
print("ADC: ")
data = []
k = 0
with open("ADC.txt") as f:
    for line in f:
        buf = line.split('        ')
        if (k == 0):
            buf[0] = buf[0][3:]
            k+=1
        data.append([float(x) for x in buf])
data = np.array(data)
data = data.transpose()
plt.plot(data[0], data[1])
plt.grid('True')
#plt.show()
#print(data[0])
#print(data[1])
#определение ошбки мастаба + индекса у нуля
itemindex = np.where(data[1]==0)
print(itemindex[0][-1])
#print(np.max(data[1]))
print("Zero error is ", 100*data[0][itemindex[0][-1]]/np.max(data[0]), "%")
#убили ошибку нуля
data[0] = data[0] - data[0][itemindex[0][-1]]
plt.plot(data[0], data[1])
#plt.show()
#ошибка масштаба

#интегральная ошибка, т.е. максимальное отклонение от идеальной кривой
fp, residuals, rank, sv, rcond = np.polyfit(data[0][itemindex[0][-1]:], data[1][itemindex[0][-1]:], 1, full=True)
#print(fp, residuals, rank, sv, rcond)
f = np.poly1d(fp)
xax = np.linspace(np.min(data[0][itemindex[0][-1]:]), np.max(data[0][itemindex[0][-1]:]), 1000)
plt.plot(xax, f(xax), label = "LSM")
print("Integ error = ", 100*np.max(np.abs(f(data[0][itemindex[0][-1]:]) - data[1][itemindex[0][-1]:]))/np.max(data[1]), "%")
plt.legend()
plt.show()











