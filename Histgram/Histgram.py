import cv2
import numpy as np
from scipy.interpolate import interp1d
import wave
from matplotlib import pyplot as plt
import struct
import sys
import os.path

args = sys.argv
PICNAME = args[1]
name, ext = os.path.splitext(PICNAME)
'''
img = cv2.imread('muse.jpg')
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
'''

img = cv2.imread(PICNAME,0)
height = img.shape[0]
width = img.shape[1]
pixel = height*width
data = []
datas = b''

hist = cv2.calcHist([img],[0],None,[256],[0,256]) #ndarray
histL = [int(n) for n in hist] #hist = hist.tolist() listにするだけだとlistの中に1x1のlistで数値が入ってしまう

x = [int(n) for n in range(1, len(histL)+1)] #xの最初を１からにした
y = histL


#f = interp1d(x, y, kind='cubric')    # ３次スプライン補間 
f = interp1d(x, y)
xnew = np.linspace(1, 256, 441)

cubricY = [int(n) for n in f(xnew)]
cubricY = [n-(max(cubricY)/2) for n in cubricY] #ヒストグラムの最大値の半分の値を引き
cubricY = [(n/max(cubricY)) * 0.3 for n in cubricY] #ヒストグラムの最大値で除して絶対値を0.3以内にする
cubricY = [int(n * 32767.0) for n in cubricY] * 100

#バイナリの列挙の文字列に直す
for n in range(len(cubricY)):
    data = [cubricY[n]]
    bindata = struct.pack("h" * len(data), *data)
    datas += bindata




#.wavとして書き出し
w = wave.Wave_write(name + ".wav")
p = (1, 2, 44100, len(datas), 'NONE', 'not compressed')
w.setparams(p)
w.writeframes(datas)
w.close()

#plt.plot(histL)
plt.plot(cubricY)
plt.xlim([0, 441])
plt.savefig(name)
#plt.show()