import math
import pylab
from matplotlib import mlab
import matplotlib.pyplot as plt
import numpy as np
import wave
import win32com.client
from numpy import int16
import xlsxwriter


file = 'sample.wav'

with wave.open(file,'r') as wav_file:
    signal = wav_file.readframes(-1)
    signal = np.fromstring(signal, 'Int16')

    channels = [[] for channel in range(wav_file.getnchannels())]
    for index, datum in enumerate(signal):
        channels[index%len(channels)].append(datum)
    channel = []
    for i in range(len(channels[0])):
        channel.append(channels[0][i]+channels[1][i])

    fs = wav_file.getframerate()
    Time = np.linspace(0, len(signal)/len(channels)/fs, num=len(signal)/len(channels))

names = ["Левый канал","Правый канал","Сумма каналов"]
ch = [channels[0],channels[1],channel]

for i in range(3):
    pylab.subplot (2, 2, i+1)
    pylab.plot (Time, ch[i])
    pylab.title (names[i])

pylab.subplot (2, 2, 4)
pylab.plot (Time, channels[0])
pylab.plot (Time, channels[1])
pylab.title ("Наложение правого канала на левый")

plt.show()


Excel = win32com.client.Dispatch("Excel.Application")
Excel.visible = False
wb = xlsxwriter.Workbook('test/test.xlsx')
sheet = wb.add_worksheet('sheetname')

for i in range(1,4):
    sheet.write(0,i-1,names[i-1]) 

for i in range(len(channels[0])):
    sheet.write(i+1,0, int16(channels[0][i]).item()) 
    sheet.write(i+1,1,int16(channels[1][i]).item()) 
    sheet.write(i+1,2,int16(channel[i]).item())
wb.close()
print('Конец')

